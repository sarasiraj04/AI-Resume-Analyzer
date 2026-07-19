import google.generativeai as genai
import os
from dotenv import load_dotenv


# Load API key
load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)


model = genai.GenerativeModel("gemini-flash-latest")


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