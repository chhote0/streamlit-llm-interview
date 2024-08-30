import streamlit as st
import numpy as np


st.title("📝Yapay Zeka ile Mülakata Hoş Geldiniz")

def user_preferences():

    position = st.selectbox('Pozisyonunuzu Seçiniz', ["Java Developer","Data Scientist","Data Analyst","Front-End Developer", 
                                       "Back-End Developer","Full-Stack Developer","Mobil Uygulama Geliştiricisi",
                                        "Yazılım Mühendisi","Gömülü Sistemler","Robotik","Veritabanı Yönetimi"])
    level = st.selectbox('Seviyenizi Seçiniz', ["Junior","Middle","Senior","Expert"])
    difficulty = st.selectbox('Mülakat Zorluğu Seçiniz', ["Kolay","Orta","Zor"])

    user_inputs = [position, level, difficulty]

    return user_inputs  #kullanıcı girdilerini liste olarak çıkarır

user_inputs = user_preferences()  #kullanıcı girdileri (Her bir bot bu verileri kullanacak)


# st.title("Hangi botla mülakat yapmak istersiniz?")


# #link fonksiyonları     (localhost adresleri değişebilir. Proje öncesi kontrol edilmeli)
# def open_llama():
#     url = 'http://localhost:8501/llama'  
#     webbrowser.open_new_tab(url)

# def open_mistral():
#     url = 'http://localhost:8501/mistral'  
#     webbrowser.open_new_tab(url)

# def open_chat_gpt():
#     url = 'http://localhost:8501/chatgpt    '  
#     webbrowser.open_new_tab(url)

# def open_mulakat():
#     url = 'http://localhost:8501/mulakat'  
#     webbrowser.open_new_tab(url)


# #Butonlar
# col1, col2, col3, col4 = st.columns(4)
# with col1:
#     st.button("Llama", on_click=open_llama)
# with col2:
#     st.button("Mistral", on_click=open_mistral)   
# with col3:
#     st.button("Chat GPT", on_click=open_chat_gpt)
# with col4:
#     st.button("Mülakat", on_click=open_mulakat)