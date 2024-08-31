import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import ast
from app import user_inputs


st.title("👉🏻Karşılıklı Mülakat👈🏻")


# Model ve prompt'u tanımla
model = OllamaLLM(model="llama3")

# Mülakat bağlamını başlat
if "interview_context" not in st.session_state:
    st.session_state.interview_context = []

# Kullanıcı inputunu temizlemek için bir durum belirleyelim
if "input_key" not in st.session_state:
    st.session_state.input_key = "user_input_0"

# İlk soru, AI tarafından sorulur
if not st.session_state.interview_context:
    initial_question = (
        f"Welcome! You have applied for a {user_inputs[0]} position at a {user_inputs[1]} difficulty level. "
        "Are you ready to start the interview?"
    )
    st.session_state.interview_context.append({"question": initial_question, "answer": None})

# Konuşma geçmişini görüntüle
st.markdown("<div style='background-color:#1a1a2e; padding:10px; border-radius:10px; max-height:300px; overflow-y:scroll;'>", unsafe_allow_html=True)

for entry in st.session_state.interview_context:
    question = entry['question']
    # Eğer soru dict veya başka bir yapıdaysa, stringe çevir ve göster
    if isinstance(question, dict):
        question = str(question)

    st.markdown(f"<p style='color:#f8f8ff; background-color:#16213e; padding:10px; border-radius:10px; margin-bottom:5px; max-width:70%; align-self:flex-start;'><strong>AI: {question}</strong></p>", unsafe_allow_html=True)
    if entry['answer']:
        st.markdown(f"<p style='color:#f8f8ff; background-color:#0f3460; padding:10px; border-radius:10px; margin-bottom:5px; max-width:70%; align-self:flex-end;'><strong>User: {entry['answer']}</strong></p>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Kullanıcıdan input al
user_input = st.text_input("Your answer:", key=st.session_state.input_key)

# Eğer kullanıcı bir input girdiyse ve 'Gönder' butonuna basarsa
if st.button("Gönder"):
    if user_input:
        # Kullanıcının cevabını bağlama ekle
        st.session_state.interview_context[-1]["answer"] = user_input

        # Cevabın doğru olup olmadığını değerlendir
        evaluation_prompt = (
            f"The candidate provided the following answer: '{user_input}' for the question '{st.session_state.interview_context[-1]['question']}'. "
            "Please evaluate if this answer is correct or incorrect, and explain briefly."
        )

        evaluation_result = model.invoke(input=evaluation_prompt)
        st.session_state.interview_context.append({"question": "Evaluation", "answer": evaluation_result})

        # Önceki bağlama göre yeni mülakat sorusu oluştur
        question_prompt = (
            f"The candidate has applied for the {user_inputs[0]} position at a {user_inputs[1]} difficulty level. "
            f"Here is the context so far: {st.session_state.interview_context}. Please provide the next interview question without extra commentary."
        )

        # Modeli çalıştırarak mülakat sorusunu al
        question_result = model.invoke(input=question_prompt)

        # Eğer result bir dict veya başka bir yapıdaysa, stringe çevir
        try:
            question_result = ast.literal_eval(question_result)
        except:
            pass

        # Yeni soruyu bağlama ekle
        st.session_state.interview_context.append({"question": question_result, "answer": None})

        # Cevap kutusunu temizlemek için input key'ini değiştir
        st.session_state.input_key = f"user_input_{len(st.session_state.interview_context)}"
        #st.experimental_rerun()



# #ana sayfaya dön
# def open_main():                   
#     url = 'http://localhost:8501'  
#     webbrowser.open_new_tab(url)

# st.button("Ana Sayfaya Dön", on_click=open_main)