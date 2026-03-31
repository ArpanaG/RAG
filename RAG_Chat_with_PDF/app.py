import streamlit as st
from rag_pipeline import build_rag

st.title("📚 Chat With PDF")

uploaded_file = st.file_uploader("Upload PDF")

if uploaded_file:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    if "qa" not in st.session_state:
        with st.spinner("Processing PDF..."):
            st.session_state.qa = build_rag("temp.pdf")

    question = st.text_input("Ask question")

    if question:
        answer = st.session_state.qa.run(question)
        st.write(answer)