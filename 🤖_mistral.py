import streamlit as st
import pandas as pd
import numpy as np
from transformers import pipeline
from mistral_inference.transformer import Transformer
from mistral_inference.generate import generate
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer
from mistral_common.protocol.instruct.messages import UserMessage
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from huggingface_hub import snapshot_download
from pathlib import Path
image_url = "linkedinicon.png"
st.title("Ⓜ Mistral")
st.info("""
Bu seansta, Mistral Yapay Zeka Mülakatçısı, pozisyonunuzla ilgili teknik becerilerinizi değerlendirecektir.

Not: Cevabınızın maksimum uzunluğu 4000 kelime olmalıdır!

Her mülakat 10-15 dakika sürecektir.
Yeni bir seans başlatmak için sayfayı yenileyin.
""")

def user_preferences():
    position = st.selectbox('Select Your Position', ["Web Development", "Mobile App Development", "Game Development", "Software Engineering",
                                                     "DevOps", "Data Science", "Machine Learning", "Artificial Intelligence",
                                                     "Natural Language Processing", "Computer Vision", "Cybersecurity",
                                                     "Ethical Hacking", "Penetration Testing", "Information Security",
                                                     "Cloud Computing", "Cloud Architecture", "Cloud Security",
                                                     "Database Administration", "Network Engineering", "UI/UX Design",
                                                     "Blockchain Development", "IoT Development", "Virtual Reality",
                                                     "Augmented Reality", "Embedded Systems", "Quantum Computing",
                                                     "Bioinformatics", "Scientific Computing", "Financial Technology",
                                                     "E-commerce Development", "Education Technology"],
                            index=st.session_state.get('selected_position_index', 0))


    # col1, col2 = st.columns([1, 3.5])
    # with col1:
    #     if st.button("Update Positions",disabled=True):
    #
    #         pass #webscraping ile linkedinden pozisyonlar çekilebilir.
    # with col2:
    #     st.image(image_url, width=40)  # Resim genişliğini ayarlayabilirsiniz

    level = st.selectbox('Select Your Level', ["Junior", "Middle", "Senior", "Expert"],
                         index=st.session_state.get('selected_level_index', 0))
    difficulty = st.selectbox('Select Interview Difficulty', ["Easy", "Medium", "Hard"],
                              index=st.session_state.get('selected_difficulty_index', 0))

    st.session_state.selected_position = position
    st.session_state.selected_level = level
    st.session_state.selected_difficulty = difficulty

    user_inputs = [position, difficulty, level]
    return user_inputs

user_inputs = user_preferences()

if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False



# Button logic

# Modeli ve tokenizer'ı sadece bir kez yüklemek için session_state kullanın
if 'model' not in st.session_state:
    mistral_models_path = Path.home().joinpath('mistral_models', '7B-Instruct-v0.3')
    mistral_models_path.mkdir(parents=True, exist_ok=True)

    # Sadece ilk seferde modeli indirip yükleyin
    snapshot_download(repo_id="mistralai/Mistral-7B-Instruct-v0.3",
                      allow_patterns=["params.json", "consolidated.safetensors", "tokenizer.model.v3"],
                      local_dir=mistral_models_path)

    st.session_state.tokenizer = MistralTokenizer.from_file(f"{mistral_models_path}/tokenizer.model.v3")
    st.session_state.model = Transformer.from_folder(mistral_models_path)

# Start the Interview butonuna basıldığında işlemleri başlatın
if st.button("Start the Interview!"):
    st.session_state.button_clicked = True  # Butona basıldığını işaretleyin

if st.session_state.get('button_clicked', False):

    # İlk soruyu oluşturma
    question_prompt = ChatCompletionRequest(
        messages=[UserMessage(
            content=f"The candidate has proficiency in {user_inputs[0]}. His expertise is {user_inputs[2]} on his job. He asks for an {user_inputs[1]} difficulty question. "
                    f"Please provide the interview question without extra commentary.")])

    # Zaten yüklenmiş olan tokenizer ve model ile devam edin
    tokenizer = st.session_state.tokenizer
    model = st.session_state.model

    tokens = tokenizer.encode_chat_completion(question_prompt).tokens

    out_tokens, _ = generate([tokens], model, max_tokens=70, temperature=0.0,
                             eos_id=tokenizer.instruct_tokenizer.tokenizer.eos_id)
    result = tokenizer.instruct_tokenizer.tokenizer.decode(out_tokens[0])

    # Soruyu gösterin
    st.text_area("Mistral:",
                 f"Hello! Welcome to our technical interview. We have reviewed the information you have provided and decided to ask you the following question: {result}")

    # Son soruyu saklayın
    st.session_state.last_question = result
    user_answer = st.text_input("Cevap:")

    if st.button("Devam"):
        # Cevabı kontrol etmek için ikinci soru isteğini oluşturma
        print(user_answer)
        question2 = ChatCompletionRequest(
            messages=[UserMessage(
                content=f"The question is {st.session_state.last_question} and user's answer is {user_answer}. "
                        f"Check the answer if it's wrong, tell me the true answer.")])

        tokens = tokenizer.encode_chat_completion(question2).tokens

        out_tokens, _ = generate([tokens], model, max_tokens=70, temperature=0.0,
                                 eos_id=tokenizer.instruct_tokenizer.tokenizer.eos_id)
        result2 = tokenizer.instruct_tokenizer.tokenizer.decode(out_tokens[0])
        print(result2)
        # Cevabın doğru olup olmadığını gösteren ikinci text_area
        st.text_area("Mistral:", f"{result2}")

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