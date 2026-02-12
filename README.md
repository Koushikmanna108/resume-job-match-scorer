# 📄 Resume–Job Match Scorer

A **Streamlit-based ATS-style web application** that analyzes how well a resume matches a given job description using **TF-IDF Vectorization and Cosine Similarity**.

This tool helps job seekers evaluate resume relevance, improve keyword alignment, and increase their chances of passing Applicant Tracking Systems (ATS).

---

## 🚀 Features

- 📤 Upload resume in **PDF format**
- 📝 Paste any **job description**
- 📊 Get a **resume–job match percentage**
- 🎯 Attractive **circular gauge visualization**
- ⚙ Uses **TF-IDF + Cosine Similarity**
- 💡 Actionable feedback based on match score
- 🎨 Clean, modern Streamlit UI

---

## 🧠 How It Works

1. Resume text is extracted from the PDF
2. Text is cleaned and stopwords are removed
3. TF-IDF vectors are created for:
   - Resume
   - Job Description
4. **Cosine Similarity** calculates the match score
5. Result is displayed with:
   - Percentage score
   - Circular gauge
   - Feedback message

---

## 🛠 Tech Stack

- **Python**
- **Streamlit** – Web UI
- **Scikit-learn** – TF-IDF & Cosine Similarity
- **NLTK** – Text preprocessing
- **PyPDF2** – PDF text extraction
- **Matplotlib** – Visualization

---

## 📂 Project Structure

resume-job-match-scorer/
│
├── app.py # Main Streamlit application
├── requirements.txt # Python dependencies
├── README.md # Project documentation


---

## 📦 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/resume-job-match-scorer.git
cd resume-job-match-scorer
2️⃣ Create a virtual environment (optional but recommended)
conda create -p venv python=3.13 -y 
conda activate venv/   
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Run the app
streamlit run app.py
📋 requirements.txt
streamlit
scikit-learn
matplotlib
nltk
PyPDF2
📊 Match Score Interpretation
Score Range	Meaning
0 – 40%	❌ Low match – Resume needs improvement
40 – 70%	⚠ Moderate match – Some improvements possible
70 – 100%	✅ Strong match – Resume aligns well
💡 Future Improvements
🧠 Missing keyword suggestions

📊 Skill-wise match breakdown

📄 Check the matching score

🌐 Deploy on Streamlit Cloud

🎨 Custom CSS theme

👨‍💻 Author
Koushik Manna
B.Tech Computer Science & Engineering

📜 License
This project is open-source and available under the MIT License.

