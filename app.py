import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="AI Interview Coach")

st.title("🤖 AI Interview Coach")
st.write("Practice interviews with AI-generated questions and smart feedback.")

role = st.text_input("Enter Role", "AI/ML Intern")

if st.button("Generate Questions"):
    prompt = f"Generate 5 interview questions for {role}"
    response = model.generate_content(prompt)
    st.write(response.text)

st.subheader("Answer Evaluation")

question = st.text_area("Interview Question")
answer = st.text_area("Your Answer")

if st.button("Evaluate Answer"):
    eval_prompt = f"""
    Interview Question:
    {question}

    Candidate Answer:
    {answer}

    Evaluate this answer and provide:
    1. Score out of 10
    2. Strengths
    3. Weaknesses
    4. Improved Answer
    """

    response = model.generate_content(eval_prompt)
    st.success(response.text)
