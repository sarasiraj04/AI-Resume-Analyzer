import streamlit as st
from pdf_reader import extract_text_from_pdf
from analyzer import analyze_resume


# Page Configuration
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# Title
st.title("📄 AI Resume Analyzer")

st.write("Upload your resume and compare it with a job description using AI.")


# Upload Resume
uploaded_file = st.file_uploader(
    "Choose your Resume (PDF)",
    type=["pdf"]
)


# Job Description Input
job_description = st.text_area(
    "💼 Paste Job Description Here",
    height=250,
    placeholder="Example: Looking for Python Developer with Machine Learning, SQL, AWS skills..."
)


# Analyze Button
if uploaded_file is not None:

    st.success("✅ Resume uploaded successfully!")

    # Extract Resume Text
    resume_text = extract_text_from_pdf(uploaded_file)


    st.subheader("📄 Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=300
    )


    if st.button("🤖 Analyze Resume"):

        if job_description.strip() == "":
            st.warning("Please enter a Job Description")

        else:

            with st.spinner("AI is analyzing your resume..."):

                analysis = analyze_resume(
                    resume_text,
                    job_description
                )


            st.subheader("🤖 AI Resume Analysis")

            st.markdown(analysis)