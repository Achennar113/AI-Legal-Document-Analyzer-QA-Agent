🧠 AI Legal Document Analyzer & Q&A Agent

An AI-powered system to analyze legal documents, summarize risks, and answer questions using LLMs + Vector Search.
Built with Streamlit (Frontend) and Django REST (Backend) using LangChain, FAISS, OCR, and Groq LLMs.

🚀 Features

📄 Upload legal documents (TXT / PDF / scanned documents)

🔍 Semantic search using FAISS vector database

🤖 Context-aware Q&A using Groq LLaMA models

🧠 Automated risk & clause summarization

🖼️ OCR support for scanned PDFs (Tesseract + OpenCV)

🌐 REST API backend (Django + DRF)

🎨 Interactive UI using Streamlit

🔐 Secure API key handling with .env

🏗️ Architecture Overview
Frontend (Streamlit)
        |
        |  REST API
        v
Backend (Django REST)
        |
        |  LangChain
        v
Vector Store (FAISS)
        |
        v
Groq LLM (LLaMA)

🧰 Tech Stack
Frontend

Streamlit

Python

Backend

Django

Django REST Framework

AI / ML

LangChain

FAISS

HuggingFace Embeddings

Groq (LLaMA 3)

OCR (for scanned documents)

Tesseract OCR

OpenCV

pdf2image

📂 Project Structure
AI-Legal-Document-Analyzer-QA-Agent/
│
├── frontend/
│   └── app.py              # Streamlit UI
│
├── backend/
│   ├── manage.py
│   ├── api/
│   │   ├── views.py        # Ingest & Q&A APIs
│   │   └── urls.py
│   └── backend/
│       ├── settings.py
│       ├── urls.py
│       └── wsgi.py
│
├── requirements.txt
├── .gitignore
└── README.md

⚙️ Setup Instructions
1️⃣ Clone Repository
git clone https://github.com/Achennar113/AI-Legal-Document-Analyzer-QA-Agent.git
cd AI-Legal-Document-Analyzer-QA-Agent

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Environment Variables

Create a .env file:

GROQ_API_KEY=your_groq_api_key_here


⚠️ Never commit .env (already ignored).

▶️ Run Backend (Django)
cd backend
python manage.py migrate
python manage.py runserver


Backend runs at:

http://127.0.0.1:8000

▶️ Run Frontend (Streamlit)
cd frontend
streamlit run app.py


Frontend runs at:

http://localhost:8501

🔌 API Endpoints
📥 Ingest Document

POST /api/ingest/

{
  "text": "This contract may be terminated with 30 days notice."
}

❓ Ask Question

POST /api/ask/

{
  "query": "What is the termination clause?"
}

📊 Example Use Cases

Legal contract review

Risk & compliance analysis

Clause extraction

Legal document summarization

Law-tech / AI research demos
