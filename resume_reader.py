import re
import streamlit as st
import pandas as pd
import numpy as np
from transformers import pipeline
from pdfminer.high_level import extract_text
import spacy
from spacy.matcher import Matcher
import pdfplumber
from io import StringIO
from streamlit_pdf_reader import pdf_reader


def extract_skills_from_resume(text, skills_list):
    skills = []

    for skill in skills_list:
        pattern = r"\b{}\b".format(re.escape(skill))
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            skills.append(skill)

    return skills

source3 = st.file_uploader("Choose a pdf file:")
text = ""
if source3:
    pdf_reader(source3)
    text = extract_text(source3)

skills_list = ['Python', 'Data Analysis', 'Machine Learning', 'Communication', 'Project Management', 'Deep Learning',
               'SQL', 'Tableau', "Inspiration",
               "Navigating challenges and change",
               "Understanding different perspectives",
               "Empathy",
               "Compassion",
               "Vision",
               "Taking responsibility",
               "Coaching",
               "Mentoring",
               "Providing feedback",
               "Integrity", "C", "C++",
               "C#",
               "Influence",
               "Resilience",
               "Empowerment",
               "Personal and professional development",
               "Machine Learning Algorithms",
               "Deep Learning Architecture",
               "Natural Language Processing (NLP)",
               "OpenCV",
               "TensorFlow",
               "PyTorch",
               "OpenAI Gym",
               "Stable Baselines",
               "RLlib",
               "Amazon Web Services (AWS)",
               "Microsoft Azure",
               "Google Cloud Platform (GCP)",
               "IBM Cloud",
               "Cloud Infrastructure",
               "Containerization",
               "Docker",
               "Kubernetes",
               "Serverless Computing",
               "AWS Lambda",
               "Azure Functions"]
extracted_skills = extract_skills_from_resume(text, skills_list)
if extracted_skills:
    st.write(extracted_skills)