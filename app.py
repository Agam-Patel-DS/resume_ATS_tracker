import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import PyPDF2 as pdf

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Gemini Pro Response
def get_gemini_response(input):
  model=genai.GenerativeModel('gemini-pro')
  response=model.generate_content(input)
  return response.text


def input_pdf_text(uploaded_file):
  pdf_reader = pdf.PdfReader(uploaded_file)  # Initialize PdfReader object
  text = ""
  for page in pdf_reader.pages:  # Use 'pages' attribute to iterate through each page
    text += page.extract_text()  # Extract text from each page
  return text

input_prompt="""
Hey act like a skilled or very experienced ATS(Application Tracking System)
with a deep understanding of tech field, software engineering, data science,
data analyst and big data engineer. Your task is to evaluate the resume based 
on the given job description. You must consider the job market is very competative
and you should provide best assistance for improving the resumes. Assign the
percentage mactching based on Job Description and the missing keywords with high accuracy.
resume={text}
description={jd}

I want response in structure of one single string - 

#### Job Description Match :
# "%"
#### Missing Keywords :
list of keywords
#### Profile Summary of Resume:
Summary
"""

st.title("Smart Application Tracking System")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste or Write your Job Description Here:")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please upload the PDF!")
submit=st.button("Submit")

if submit:
  if uploaded_file is not None:
    text=input_pdf_text(uploaded_file)
    response=get_gemini_response(input_prompt)
    st.write(response)



