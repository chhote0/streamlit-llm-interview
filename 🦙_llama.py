import streamlit as st
import pandas as pd
import numpy as np
from transformers import pipeline

st.title("🦙Llama")

st.info("""
Bu seansta, Llama Yapay Zeka Mülakatçısı, pozisyonunuzla ilgili teknik becerilerinizi değerlendirecektir.

Not: Cevabınızın maksimum uzunluğu 4000 kelime olmalıdır!

Her mülakat 10-15 dakika sürecektir.
Yeni bir seans başlatmak için sayfayı yenileyin.
""")


if st.button("Mülakata Başla!"):
    st.text_area("Llama:", "Merhaba! Teknik mülakatımıza hoş geldiniz. İlk sorumuz: Veri biliminde en sık kullandığınız 3 kütüphane nelerdir ve neden bu kütüphaneleri tercih edersiniz?")

    # Buraya döngü ve yeni soru oluşturma kısmı gelecek
    while True:
        user_answer = st.text_area("Cevap:")
        if st.button("Devam"):
            ""
            # Llama'ya cevabı gönder ve yeni soru al (bu kısım henüz tamamlanmadı)
            # Örneğin:
            # yeni_soru = llama_model.generate_question(user_answer)
            # st.text_area("Llama:", yeni_soru)

                
        else:
            break




# # Doğru cevapları içeren bir DataFrame (örnek)
# correct_answers = pd.DataFrame({'question': ['Veri biliminde en sık kullandığınız 3 kütüphane nelerdir?', ...],
#                                'answer': ['pandas, numpy, scikit-learn', ...]})

# # NLP modeli yükleme (örnek: BERT)
# nlp = pipeline("feature-extraction", model="bert-base-uncased")

# # Cevap değerlendirmesi
# if st.button("Değerlendir"):
#     user_answer = st.text_area("Cevap:")
#     # Doğru cevabı bul
#     correct_answer = correct_answers[correct_answers['question'] == "Veri biliminde en sık kullandığınız 3 kütüphane nelerdir?"]['answer'].values[0]
#     # Semantik benzerlik hesaplama
#     similarity_score = nlp(user_answer)[0].dot(nlp(correct_answer)[0]) / (np.linalg.norm(nlp(user_answer)[0]) * np.linalg.norm(nlp(correct_answer)[0]))
#     # Puanlama
#     if similarity_score > 0.8:
#         st.success("Harika bir cevap!")
#     else:
#         st.warning("Cevabınızda eksiklikler olabilir.")


# #ana sayfaya dön
# def open_main():                   
#     url = 'http://localhost:8501'  
#     webbrowser.open_new_tab(url)

# st.button("Ana Sayfaya Dön", on_click=open_main)