import streamlit as st
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# ---------------- NLTK Downloads ----------------
nltk.download("punkt")
nltk.download("stopwords")

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Resume–Job Match Scorer",
    page_icon="📄",
    layout="wide"
)

# ---------------- Helper Functions ----------------
def extract_text_from_pdf(uploaded_file):
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return ""

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def remove_stopwords(text):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)
    return " ".join([w for w in words if w not in stop_words])

def calculate_similarity(resume_text, job_description):
    resume_processed = remove_stopwords(clean_text(resume_text))
    job_processed = remove_stopwords(clean_text(job_description))
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([resume_processed, job_processed])
    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0] * 100
    return round(score, 2)

# ---------------- Gauge Function ----------------
def draw_gauge(score):
    fig, ax = plt.subplots(figsize=(4, 4))

    sizes = [score, 100 - score]

    if score < 40:
        colors = ["#ff4b4b", "#e0e0e0"]
    elif score < 70:
        colors = ["#ffa726", "#e0e0e0"]
    else:
        colors = ["#0f9d58", "#e0e0e0"]

    ax.pie(
        sizes,
        startangle=90,
        colors=colors,
        wedgeprops={"width": 0.35}
    )

    ax.text(
        0, 0,
        f"{score:.1f}%",
        ha="center",
        va="center",
        fontsize=22,
        fontweight="bold"
    )

    ax.set_title("Resume Match Score")
    ax.axis("equal")

    return fig

# ---------------- Main App ----------------
def main():

    # -------- Header --------
    st.markdown("""
    <div style="text-align:center;">
        <h1>📄 Resume–Job Match Scorer</h1>
        <p style="font-size:18px;">
            Instantly see how well your resume matches a job description 🚀
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # -------- Sidebar --------
    with st.sidebar:
        st.markdown("## 📌 About")
        st.write("""
        ✔ ATS-style resume analysis  
        ✔ TF-IDF + Cosine Similarity  
        ✔ Resume improvement insights  
        """)

        st.divider()

        st.markdown("## ⚙ How It Works")
        st.write("""
        1️⃣ Upload resume (PDF)  
        2️⃣ Paste job description  
        3️⃣ Click Analyze  
        4️⃣ View match score  
        """)

        st.divider()
        st.success("💡 Tip: Add missing keywords to boost ATS score")

    # -------- Input Layout --------
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📤 Upload Resume")
        uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

    with col2:
        st.markdown("### 📝 Job Description")
        job_description = st.text_area(
            "Paste job description",
            height=220,
            placeholder="Enter job requirements, skills, responsibilities..."
        )

    st.divider()

    # -------- Analyze Button --------
    analyze = st.button("🔍 Analyze Match", use_container_width=True)

    if analyze:
        if not uploaded_file:
            st.warning("⚠ Please upload your resume.")
            return
        if not job_description:
            st.warning("⚠ Please paste the job description.")
            return

        with st.spinner("🔎 Analyzing your resume..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            if not resume_text:
                st.error("Could not extract text from PDF.")
                return

            similarity_score = calculate_similarity(resume_text, job_description)

        # -------- Results --------
        st.subheader("📊 Match Results")
        st.metric("Match Score", f"{similarity_score}%")

        fig = draw_gauge(similarity_score)
        st.pyplot(fig)

        if similarity_score < 40:
            st.error("❌ Low Match – Consider tailoring your resume.")
        elif similarity_score < 70:
            st.warning("⚠ Good Match – Some improvements possible.")
        else:
            st.success("✅ Excellent Match – Strong alignment!")

# ---------------- Run App ----------------
if __name__ == "__main__":
    main()
