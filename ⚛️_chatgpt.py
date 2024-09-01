import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

st.title("GPT-2 ile Teknik Mülakat Simülasyonu")

# GPT-2 modelini ve tokenizer'ı Hugging Face'ten yükleyin
model_name = "openai-community/gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)


def get_user_selection():
    """
    Kullanıcının pozisyon, seviye ve mülakat zorluk seviyesini seçmesini sağlar.
    """
    if 'selected_position' not in st.session_state:
        st.session_state.selected_position = "Yazılım Geliştirici"
    if 'selected_level' not in st.session_state:
        st.session_state.selected_level = "Junior"

    position = st.selectbox('Pozisyon Seçin', [
        "Yazılım Geliştirici", "Veri Bilimci", "Makine Öğrenimi Mühendisi", "Sistem Mühendisi",
        "Ağ Mühendisi", "Siber Güvenlik Uzmanı", "Mobil Geliştirici", "Oyun Geliştirici"],
                            index=st.session_state.get('selected_position_index', 0))

    level = st.selectbox('Deneyim Seviyesi', ["Junior", "Orta", "Kıdemli", "Uzman"],
                         index=st.session_state.get('selected_level_index', 0))

    st.session_state.selected_position = position
    st.session_state.selected_level = level

    return [position, level]


user_selection = get_user_selection()

if "interview_started" not in st.session_state:
    st.session_state.interview_started = False
if "current_question" not in st.session_state:
    st.session_state.current_question = None
if "user_input" not in st.session_state:
    st.session_state.user_input = ""
if "interview_log" not in st.session_state:
    st.session_state.interview_log = []
if "interview_context" not in st.session_state:
    st.session_state.interview_context = []


def generate_interview_question(position, level):
    # Generate a question based on the user's selected position and level
    question_prompt = (
        f"The candidate is applying for a position in {position} at the {level} level. "
        f"Here is the context so far: {st.session_state.interview_context}. "
        f"Please provide the next interview question."
    )

    inputs = tokenizer.encode(question_prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=500, max_new_tokens=100, pad_token_id=tokenizer.eos_token_id)
    question = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Soru ve bağlamı güncelle
    st.session_state.interview_context.append(question)
    return question


def evaluate_answer(question, user_answer):
    """
    Kullanıcının verdiği cevabı değerlendirir ve doğru ya da yanlış olduğunu belirtir.
    Yanlışsa doğrusunu sağlar.
    """
    prompt = f"The question was: {question}\nThe answer provided is: {user_answer}\nIs the answer correct? If not, please provide the correct answer."
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=500, max_new_tokens=100, pad_token_id=tokenizer.eos_token_id)
    evaluation = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return evaluation


if not st.session_state.interview_started:
    if st.button("Mülakatı Başlat!"):
        st.session_state.interview_started = True
        st.session_state.current_question = generate_interview_question(user_selection[0], user_selection[1])
else:
    st.info("Bu oturumda GPT-2 modeli ile teknik mülakat yapılacaktır.")

    if st.session_state.current_question is None:
        st.session_state.current_question = generate_interview_question(user_selection[0], user_selection[1])

    st.text_area("GPT-2 Sorusu:", st.session_state.current_question, key="current_question_display", height=150)

    st.session_state.user_input = st.text_area("Cevabınızı Girin:", st.session_state.user_input, key="user_input_key",
                                               height=150)

    if st.button("Değerlendir"):
        if st.session_state.user_input.strip():
            st.session_state.interview_log.append({
                "question": st.session_state.current_question,
                "answer": st.session_state.user_input
            })

            feedback = evaluate_answer(st.session_state.current_question, st.session_state.user_input)
            st.write("Değerlendirme:", feedback)

            st.session_state.user_input = ""
            st.session_state.current_question = generate_interview_question(user_selection[0], user_selection[1])
    else:
        st.text("Mülakat devam ediyor, lütfen cevabınızı girin.")
