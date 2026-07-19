# 📄 AI Resume Analyzer using Gemini AI

An AI-powered Resume Analyzer built with **Python**, **Streamlit**, and **Google Gemini AI**. This application extracts text from PDF resumes, compares them with a job description, calculates an ATS match score, identifies missing skills, and provides AI-powered suggestions to improve the resume.

---

## 🚀 Features

- 📄 Upload Resume in PDF format
- 🔍 Extract text from PDF automatically
- 🤖 AI Resume Analysis using Google Gemini
- 📊 ATS Score Prediction
- 💼 Resume vs Job Description Matching
- ✅ Matching Skills Detection
- ❌ Missing Skills Identification
- 💡 Resume Improvement Suggestions
- ⚡ Simple and User-Friendly Interface

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Framework
- Streamlit

### AI Model
- Google Gemini API

### Libraries
- google-generativeai
- PyPDF2
- python-dotenv

---

## 📂 Project Structure

```
AI_Resume_Analyzer/
│
├── app.py
├── analyzer.py
├── pdf_reader.py
├── prompt.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env (Not uploaded to GitHub)
│
└── screenshots/
    ├── home.jpeg
    ├── extracted_text.jpeg
    └── analysis.jpeg
```

---

## 📸 Application Preview

### 🏠 Home Page

![Home Page](screenshots/home.jpeg)

---

### 📄 Resume Text Extraction

![Resume Extraction](screenshots/extracted_text.jpeg)

---

### 🤖 AI Resume Analysis

![AI Resume Analysis](screenshots/analysis.jpeg)

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sarasiraj04/AI-Resume-Analyzer.git
```

### 2. Navigate to the Project Folder

```bash
cd AI-Resume-Analyzer
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Create a `.env` File

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

### 7. Run the Application

```bash
streamlit run app.py
```

---

## 🔮 Future Improvements

- Resume Ranking System
- Multiple Resume Comparison
- Resume PDF Report Generation
- Download Analysis as PDF
- Skill Recommendation Engine
- Cloud Deployment

---

## 👩‍💻 Author

**Sara**

B.Tech Artificial Intelligence & Data Science

GitHub: https://github.com/sarasiraj04

---

⭐ If you like this project, don't forget to star the repository!