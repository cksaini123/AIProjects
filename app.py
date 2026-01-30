import streamlit as st
import subprocess

st.title("AI Learning Assistant (Local & Free)")
st.set_page_config(page_title="AI Tutor", layout="centered")

st.sidebar.header("About")
st.sidebar.write("Built by Chandrakanta")

topic = st.text_input("Enter a topic to learn")

def ask_ai(prompt):
    result = subprocess.run(
        ["ollama", "run", "llama3", prompt],
        capture_output=True,
        text=True
    )
    return result.stdout

if st.button("Explain"):
    if topic:
        with st.spinner("Thinking like a teacher..."):
            prompt = f"""
            You are a patient teacher.
            Explain {topic} in simple terms.
            Give:
            1. Easy explanation
            2. One example
            3. 3 practice questions
            """
            answer = ask_ai(prompt)
            st.write(answer)
    else:
        st.warning("Please enter a topic")