import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env (for local development)
load_dotenv()

# Get API Key
api_key = os.getenv("GOOGLE_API_KEY")

# If running on Streamlit Cloud, use Secrets
if not api_key:
    api_key = st.secrets["GOOGLE_API_KEY"]

# Configure Gemini
genai.configure(api_key=api_key)

# Load Model
model = genai.GenerativeModel("gemini-2.0-flash")


def analyze_resume(resume_text, job_description):

    prompt = f"""
You are an expert ATS (Applicant Tracking System) Resume Analyzer.

Analyze the candidate resume against the given job description.

Provide the following:

1. ATS Match Score out of 100

2. Matching Skills:
- List skills from resume that match the job description

3. Missing Skills:
- List important skills required in job description but missing in resume

4. Resume Strengths:
- Explain strong points

5. Resume Weaknesses:
- Explain problems affecting ATS score

6. Improvement Suggestions:
- Give practical suggestions to improve the resume

7. Final Hiring Recommendation:
- Suitable / Needs Improvement / Not Suitable

====================
RESUME:
====================

{resume_text}

====================
JOB DESCRIPTION:
====================

{job_description}
"""

    response = model.generate_content(prompt)
    return response.text