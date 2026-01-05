import os
import cv2
import pytesseract
import streamlit as st
from dotenv import load_dotenv
from tempfile import NamedTemporaryFile
from PIL import Image
from pdf2image import convert_from_path

from langchain.schema import Document
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# -----------------------------
# OCR HELPERS
# -----------------------------
def extract_text_from_image(image: Image.Image) -> str:
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    text = pytesseract.image_to_string(img)
    return text

def extract_text_from_pdf(pdf_path: str) -> str:
    pages = convert_from_path(pdf_path)
    full_text = ""

    for page in pages:
        text = pytesseract.image_to_string(page)
        full_text += text + "\n"

    return full_text

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="AI Legal Document Analyzer", layout="wide")
st.title("⚖️ AI Legal Document Analyzer & Q&A Agent")

uploaded_file = st.file_uploader(
    "Upload TXT / PDF (scanned or digital)",
    type=["txt", "pdf"]
)

if uploaded_file:
    with NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        file_path = tmp.name

    st.success("✅ File uploaded")

    # -----------------------------
    # TEXT EXTRACTION
    # -----------------------------
    extracted_text = ""

    try:
        if uploaded_file.name.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                extracted_text = f.read()

        elif uploaded_file.name.endswith(".pdf"):
            extracted_text = extract_text_from_pdf(file_path)

        else:
            st.error("Unsupported file format")
            st.stop()

    except Exception as e:
        st.error(f"Text extraction failed: {e}")
        st.stop()

    if not extracted_text.strip():
        st.error("❌ No text could be extracted")
        st.stop()

    # -----------------------------
    # DOCUMENT CHUNKING
    # -----------------------------
    documents = [Document(page_content=extracted_text)]

    splitter = CharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    chunks = splitter.split_documents(documents)

    st.write(f"📑 Chunks created: {len(chunks)}")

    # -----------------------------
    # EMBEDDINGS + FAISS
    # -----------------------------
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    st.success("✅ FAISS vector store created")

    # -----------------------------
    # LLM (Groq)
    # -----------------------------
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0
    )

    # -----------------------------
    # Q&A
    # -----------------------------
    query = st.text_input("Ask a legal question:")

    if query:
        docs = vectorstore.similarity_search(query, k=4)

        context = "\n\n".join(d.page_content for d in docs)

        prompt = f"""
You are an AI Legal Document Analyzer.

- Answer strictly from the context
- Identify risks if present
- If information is missing, say "Not found in document"

Context:
{context}

Question:
{query}
"""

        response = llm.invoke(prompt)

        st.subheader("🔍 Answer")
        st.write(response.content)

        with st.expander("📄 Source Evidence"):
            for i, d in enumerate(docs, 1):
                st.markdown(f"**Chunk {i}:**")
                st.write(d.page_content[:500])

    os.remove(file_path)
