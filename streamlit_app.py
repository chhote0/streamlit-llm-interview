import streamlit as st

giris_page = st.Page(
    page = "app.py",
    title = "Teknik Mülakata Giriş",
    icon = ":material/account_circle:",
    default = True,    
)

llama_page = st.Page(
    page = "llama.py",
    title = "llama",
    icon = ":material/account_circle:",
    default = True,    
)

mistral_page = st.Page(
    page = "mistral.py",
    title = "mistral",
    icon = ":material/account_circle:",
    default = True,    
)


gpt_page = st.Page(
    page = "chatgpt.py",
    title = "ChatGPT",
    icon = ":material/account_circle:",
    default = True,    
)

mulakat_page = st.Page(
    page = "mulakat.py",
    title = "Karşılıklı Mülakat",
    icon = ":material/account_circle:",
    default = True,    
)



pg = st.navigation(pages=[st.Page("app.py"), st.Page("llama.py"), st.Page("mistral.py"), 
                          st.Page("chatgpt.py"), st.Page("mulakat.py")])

pg.run()