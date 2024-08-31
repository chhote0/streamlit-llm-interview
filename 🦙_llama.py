import streamlit as st
from langchain_ollama import OllamaLLM

# Sample CV data for the candidate
cv_data = {
    "candidate_name": "Ahmet",
    "skills": [
        {"skill": "Python", "proficiency": "intermediate"},
        {"skill": "SQL", "proficiency": "advanced"},
        {"skill": "Machine Learning", "proficiency": "beginner"}
    ],
    "interests": ["data science", "artificial intelligence"],
    "potential_roles": ["data analyst", "machine learning engineer"],
    "education": {
        "degree": "Bachelor of Computer Science",
    }
}

# Initialize session state variables if not already set
if "current_question" not in st.session_state:
    st.session_state.current_question = None
if "user_input" not in st.session_state:
    st.session_state.user_input = ""
if "interview_context" not in st.session_state:
    st.session_state.interview_context = []

# Define the LLM model
model = OllamaLLM(model="ollama_prompt")

def generate_question(cv_data):
    # Generate a question based on the candidate's CV data
    question_prompt = (
        f"The candidate has proficiency in {cv_data['skills'][0]['skill']} and an interest in {cv_data['interests'][0]}. "
        f"Here is the context so far: {st.session_state.interview_context}. Please provide the next interview question."
    )
    return model.invoke(input=question_prompt)

def provide_feedback(user_answer):
    # Provide feedback on the candidate's response
    feedback_prompt = (
                f"Provide direct feedback on the candidate's response: '{user_answer}'. "
                f"Focus only on providing a clear and concise answer, correcting if needed."
            )
    return model.invoke(input=feedback_prompt)

# Streamlit UI
st.title("Llama Yapay Zeka Mülakatçısı")

st.info("""
Bu seansta, Llama Yapay Zeka Mülakatçısı, pozisyonunuzla ilgili teknik becerilerinizi değerlendirecektir.
Not: Cevabınızın maksimum uzunluğu 4000 kelime olmalıdır!
Her mülakat 10-15 dakika sürecektir.
Yeni bir seans başlatmak için sayfayı yenileyin.
""")

# Display the current question or generate a new one if needed
if st.session_state.current_question is None:
    st.session_state.current_question = generate_question(cv_data)

# Show the current question
st.text_area("Llama:", st.session_state.current_question, key="current_question_display", height=150)

# Get the user's answer
st.session_state.user_input = st.text_area("Cevabınız:", st.session_state.user_input, key="user_input_key", height=150)

if st.button("Devam"):
    if st.session_state.user_input.strip():  # Only proceed if there's input
        # Store the user's answer and feedback in the interview context
        st.session_state.interview_context.append({
            "question": st.session_state.current_question,
            "answer": st.session_state.user_input
        })

        # Provide feedback based on the answer
        feedback = provide_feedback(st.session_state.user_input)
        st.write("Llama Feedback:", feedback)

        # Clear the user's input and prepare for the next question
        st.session_state.user_input = ""  # Reset user input
        st.session_state.current_question = generate_question(cv_data)  # Get the next question
else:
    st.text("Mülakat sorusu devam ediyor. Lütfen cevabınızı girin.")
