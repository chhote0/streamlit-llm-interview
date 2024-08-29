import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


st.title("Karşılıklı Mülakat")


template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

# Model ve prompt'u tanımla
model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Konuşma geçmişini saklamak için bir değişken
if "context" not in st.session_state:
    st.session_state.context = ""

# İlk soru, AI tarafından sorulur
if not st.session_state.context:
    initial_question = "Mülakat yapmak ister misin?"
    st.session_state.context = f"AI: {initial_question}"
    st.markdown(f"<p style='color:lightblue;'><strong>AI: {initial_question}</strong></p>", unsafe_allow_html=True)

# Kullanıcıdan input al
user_input = st.text_input("You:")

# Eğer kullanıcı bir input girdiyse ve 'Gönder' butonuna basarsa
if st.button("Gönder"):
    if user_input:
        # Modelden cevap al
        result = chain.invoke({"context": st.session_state.context, "question": user_input})

        # Konuşma geçmişini güncelle
        st.session_state.context += f"\nUser: {user_input}\nAI: {result}"

# Konuşma geçmişini görüntüle
if st.session_state.context:
    st.write("## Konuşma Geçmişi")
    st.markdown("<div style='background-color:#f1f1f1; padding:10px; border-radius:10px; max-height:300px; overflow-y:scroll;'>", unsafe_allow_html=True)

    for line in st.session_state.context.split("\n"):
        if line.startswith("User:"):
            st.markdown(f"<p style='color:white; background-color:#007bff; padding:10px; border-radius:10px; margin-bottom:5px; max-width:70%; align-self:flex-end;'><strong>{line}</strong></p>", unsafe_allow_html=True)
        elif line.startswith("AI:"):
            st.markdown(f"<p style='color:lightblue; background-color:#f0f0f0; padding:10px; border-radius:10px; margin-bottom:5px; max-width:70%; align-self:flex-start;'><strong>{line}</strong></p>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# #ana sayfaya dön
# def open_main():                   
#     url = 'http://localhost:8501'  
#     webbrowser.open_new_tab(url)

# st.button("Ana Sayfaya Dön", on_click=open_main)