import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import ast

st.title("👉🏻Interview👈🏻")

# Initialize the model outside of the button clicks to make it globally accessible
model = OllamaLLM(model="llama3")

def user_preferences():
    position = st.selectbox('Select Your Position', ["Web Development","Mobile App Development","Game Development","Software Engineering",
    "DevOps","Data Science","Machine Learning","Artificial Intelligence","Natural Language Processing","Computer Vision","Cybersecurity",
    "Ethical Hacking","Penetration Testing","Information Security","Cloud Computing","Cloud Architecture","Cloud Security","Database Administration",
    "Network Engineering","UI/UX Design","Blockchain Development","IoT Development","Virtual Reality","Augmented Reality","Embedded Systems",
    "Quantum Computing","Bioinformatics","Scientific Computing","Financial Technology","E-commerce Development","Education Technology"],
                            index=st.session_state.get('selected_position_index', 0))
    level = st.selectbox('Select Your Level', ["Junior", "Middle", "Senior", "Expert"],
                         index=st.session_state.get('selected_level_index', 0))
    difficulty = st.selectbox('Select Interview Difficulty', ["Easy", "Medium", "Hard"],
                              index=st.session_state.get('selected_difficulty_index', 0))

    st.session_state.selected_position = position
    st.session_state.selected_level = level
    st.session_state.selected_difficulty = difficulty

    user_inputs = [position, difficulty]
    return user_inputs

user_inputs = user_preferences()

if st.button("Start Interview!"):
    # Initialize interview context if not already present
    if "interview_context" not in st.session_state:
        st.session_state.interview_context = []

    # Initialize the input key if not already present
    if "input_key" not in st.session_state:
        st.session_state.input_key = "user_input_0"

    # Start the interview with the first question
    if not st.session_state.interview_context:
        initial_question = (
            f"Welcome! You have applied for a {user_inputs[0]} position at a {user_inputs[1]} difficulty level. "
            "Are you ready to start the interview?"
        )
        st.session_state.interview_context.append({"role": "AI", "content": initial_question})

# Display the interview conversation
st.markdown("<div style='padding:10px; border-radius:10px; max-height:300px; overflow-y:scroll;'>", unsafe_allow_html=True)

for entry in st.session_state.get('interview_context', []):
    role = entry['role']
    content = entry['content']
    if isinstance(content, dict):
        content = str(content)
    
    # Display differently based on whether it's AI or user content
    if role == "AI":
        st.markdown(f"<p style='color:#f8f8ff; background-color:#16213e; padding:10px; border-radius:10px; margin-bottom:5px; max-width:70%; align-self:flex-start;'><strong>AI: {content}</strong></p>", unsafe_allow_html=True)
    else:
        st.markdown(f"<p style='color:#f8f8ff; background-color:#0f3460; padding:10px; border-radius:10px; margin-bottom:5px; max-width:70%; align-self:flex-end;'><strong>User: {content}</strong></p>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Collect user input
user_input = st.text_input("Your answer:", key=st.session_state.get('input_key', 'user_input_0'))

# Disable "Gönder" button if the interview hasn't started
if st.session_state.get('interview_context'):
    if st.button("Send"):
        if user_input:
            # Add the user's answer to the interview context
            st.session_state.interview_context[-1]["answer"] = user_input
            st.session_state.interview_context.append({"role": "User", "content": user_input})

            # Evaluate the answer
            evaluation_prompt = (
                f"The candidate provided the following answer: '{user_input}' for the question '{st.session_state.interview_context[-1]['content']}'. "
                "Please evaluate if this answer is correct or incorrect, and explain briefly."
            )

            evaluation_result = model.invoke(input=evaluation_prompt)
            st.session_state.interview_context.append({"role": "AI", "content": evaluation_result})

            # Generate the next interview question
            question_prompt = (
                f"The candidate has applied for the {user_inputs[0]} position at a {user_inputs[1]} difficulty level. "
                f"Here is the context so far: {st.session_state.interview_context}. Please provide the next interview question in plain text without extra commentary."
            )

            question_result = model.invoke(input=question_prompt)

            try:
                question_result = ast.literal_eval(question_result)
            except:
                pass

            # Add the new question to the interview context
            st.session_state.interview_context.append({"role": "AI", "content": question_result})

            # Clear the input box by updating the input key
            st.session_state.input_key = f"user_input_{len(st.session_state.interview_context)}"
            st.rerun()
else:
    st.button("Send", disabled=True)

