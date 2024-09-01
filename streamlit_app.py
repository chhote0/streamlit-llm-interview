import streamlit as st
import pandas as pd
import numpy as np


giris_page = st.Page(
    page = "_app.py",
    title = "Teknik Mülakata Giriş",
    icon = ":material/account_circle:",
    default = True,    
)

llama_page = st.Page(
    page = "🦙_llama.py",
    title = "llama",
    icon = ":material/account_circle:",
    default = True,    
)

mistral_page = st.Page(
    page = "🤖_mistral.py",
    title = "mistral",
    icon = ":material/account_circle:",
    default = True,    
)


gpt_page = st.Page(
    page = "⚛️_chatgpt.py",
    title = "ChatGPT",
    icon = ":material/account_circle:",
    default = True,    
)

mulakat_page = st.Page(
    page = "🗣️_mulakat.py",
    title = "Karşılıklı Mülakat",
    icon = ":material/account_circle:",
    default = True,    
)
mulakat_page = st.Page(
    page = "resume_reader.py",
    title = "Karşılıklı Mülakat",
    icon = ":material/account_circle:",
    default = True,
)


pg = st.navigation(pages=[st.Page("_app.py"), st.Page("🦙_llama.py"), st.Page("🤖_mistral.py"),
                          st.Page("⚛️_chatgpt.py"), st.Page("🗣️_mulakat.py"), st.Page("resume_reader.py")])

pg.run()