import streamlit as st
import numpy as np
import time



st.title("Yapay Zeka ile Mülakata Hoş Geldiniz")

st.selectbox('Pozisyonunuzu Seçiniz', ["Java Developer","Data Scientist","Data Analyst","Front-End Developer", 
                                       "Back-End Developer","Full-Stack Developer","Mobil Uygulama Geliştiricisi",
                                        "Yazılım Mühendisi","Gömülü Sistemler","Robotik","Veritabanı Yönetimi"])

st.selectbox('Seviyenizi Seçiniz', ["Junior","Middle","Senior","Expert"])

st.selectbox('Mülakat Zorluğu Seçiniz', ["Kolay","Orta","Zor"])

st.title("Hangi botla mülakat yapmak istersiniz?")




#selected = st.sidebar.selectbox("**Bot Seçiniz**", ["Llama", "Mistral", "Chat GPT", "Bla Bla"])



if 'bot_clicked' not in st.session_state:
    st.session_state.bot_clicked = False 

# Bot ekranları
def llama_screen():
    st.session_state.bot_clicked = True
    st.title("Llama Ekranı")
    st.write("Bu Llama modeliyle yapacağınız mülakat ekranı.")
    # Llama modeliyle ilgili işlemler buraya gelecek

def mistral_screen():
    st.session_state.bot_clicked = True
    st.title("mistral Ekranı")
    st.write("Bu mistral modeliyle yapacağınız mülakat ekranı.")
    # mistral modeliyle ilgili işlemler buraya gelecek

def chat_gpt_screen():
    st.session_state.bot_clicked = True
    st.title("chat_gpt Ekranı")
    st.write("Bu chat_gpt modeliyle yapacağınız mülakat ekranı.")
    # chat_gpt modeliyle ilgili işlemler buraya gelecek

def bla_bla_screen():
    st.session_state.bot_clicked = True
    st.title("bla_bla Ekranı")
    st.write("Bu bla_bla modeliyle yapacağınız mülakat ekranı.")
    # bla_bla modeliyle ilgili işlemler buraya gelecek


col1, col2, col3, col4 = st.columns(4)
with col1:
    st.button("Llama", on_click=llama_screen)
with col2:
    st.button("Mistral", on_click=mistral_screen)
with col3:
    st.button("Chat GPT", on_click=chat_gpt_screen)
with col4:
    st.button("Bla Bla", on_click=bla_bla_screen)



# if selected == "Llama":
#     llama_screen()
# elif selected == "Mistral":
#     mistral_screen()
# elif selected == "Chat GPT":
#     chat_gpt_screen()
# else:
#     bla_bla_screen()

