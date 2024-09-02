import streamlit as st
from langchain_ollama import OllamaLLM

st.title("🦙Llama")

# Initialize the model outside of the button clicks to make it globally accessible
model = OllamaLLM(model="llama3")

def user_preferences():
    position = st.selectbox('Select Your Position', [
        "Web Development", "Mobile App Development", "Game Development", 
        "Software Engineering", "DevOps", "Data Science", 
        "Machine Learning", "Artificial Intelligence", 
        "Natural Language Processing", "Computer Vision", 
        "Cybersecurity", "Ethical Hacking", "Penetration Testing", 
        "Information Security", "Cloud Computing", "Cloud Architecture", 
        "Cloud Security", "Database Administration", "Network Engineering", 
        "UI/UX Design", "Blockchain Development", "IoT Development", 
        "Virtual Reality", "Augmented Reality", "Embedded Systems", 
        "Quantum Computing", "Bioinformatics", "Scientific Computing", 
        "Financial Technology", "E-commerce Development", "Education Technology"
    ], index=st.session_state.get('selected_position_index', 0))

    level = st.selectbox('Select Your Level', [
        "Junior", "Middle", "Senior", "Expert"
    ], index=st.session_state.get('selected_level_index', 0))

    difficulty = st.selectbox('Select Interview Difficulty', [
        "Easy", "Medium", "Hard"
    ], index=st.session_state.get('selected_difficulty_index', 0))

    st.session_state.selected_position = position
    st.session_state.selected_level = level
    st.session_state.selected_difficulty = difficulty

    return position, level, difficulty

position, level, difficulty = user_preferences()

# Initialize session state variables if not already set
if "interview_started" not in st.session_state:
    st.session_state.interview_started = False
if "current_question" not in st.session_state:
    st.session_state.current_question = None
if "user_input" not in st.session_state:
    st.session_state.user_input = ""
if "interview_context" not in st.session_state:
    st.session_state.interview_context = []

def generate_question(position, level, difficulty):
    # Generate a question based on the user's selected position, level, and difficulty
    question_prompt = (
        f"The candidate is applying for a position in {position} at the {level} level. "
        f"The interview difficulty is set to {difficulty}. "
        f"Here is the context so far: {st.session_state.interview_context}. "
        f"Please provide the next interview question."
    )
    return model.invoke(input=question_prompt)

def provide_feedback(user_answer):
    # Provide feedback on the candidate's response
    feedback_prompt = (
        f"Provide direct feedback on the candidate's response: '{user_answer}'. "
        f"Focus only on providing a clear and concise answer, correcting if needed."
    )
    return model.invoke(input=feedback_prompt)

# Display "Start Interview!" button and start the interview when clicked
if not st.session_state.interview_started:
    if st.button("Start Interview!"):
        st.session_state.interview_started = True
        st.session_state.current_question = generate_question(position, level, difficulty)
else:
    st.info("""
    In this session, the Llama AI Interviewer will assess your technical skills related to your position.

    Note: Your answer must be 4000 words long!

    Each interview will last 10-15 minutes.
    Refresh the page to start a new session.
    """)

    # Display the current question or generate a new one if needed
    if st.session_state.current_question is None:
        st.session_state.current_question = generate_question(position, level, difficulty)

    # Show the current question
    st.text_area("Llama:", st.session_state.current_question, key="current_question_display", height=150)

    # Get the user's answer
    st.session_state.user_input = st.text_area("Your Answer:", st.session_state.user_input, key="user_input_key", height=150)

    if st.button("Continue"):
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
            st.session_state.current_question = generate_question(position, level, difficulty)  # Get the next question

    else:
        st.text("The interview question is still ongoing. Please input your answer.")

