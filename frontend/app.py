import streamlit as st
import requests
import os
from tempfile import NamedTemporaryFile
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = "http://localhost:8000/api"

st.set_page_config(page_title="AI Legal Document Analyzer", layout="wide")
st.title("⚖️ AI Legal Document Analyzer & Q&A")

uploaded_file = st.file_uploader("Upload TXT file", type=["txt"])

if uploaded_file:
    with NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        file_path = tmp.name

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

    res = requests.post(
        f"{BACKEND_URL}/ingest/",
        json={"text": text}
    )

    st.success("Document indexed")

    query = st.text_input("Ask a legal question:")

    if query:
        ans = requests.post(
            f"{BACKEND_URL}/ask/",
            json={"query": query}
        )
        st.subheader("Answer")
        st.write(ans.json()["answer"])

    os.remove(file_path)
