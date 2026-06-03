import streamlit as st

st.set_page_config(page_title="AI Interview Coach")

st.title("🤖 AI Interview Coach")

st.write("Upload your resume, generate interview questions and get AI feedback.")

role = st.text_input("Enter Role", "AI/ML Intern")

if st.button("Generate Questions"):
    st.write("1. Tell me about yourself.")
    st.write("2. Explain one project from your resume.")
    st.write("3. Why are you interested in this role?")
    st.write("4. What are your strengths?")
    st.write("5. Why should we hire you?")

question = st.text_area("Interview Question")
answer = st.text_area("Your Answer")

if st.button("Evaluate Answer"):
    st.success("AI Evaluation will appear here.")
