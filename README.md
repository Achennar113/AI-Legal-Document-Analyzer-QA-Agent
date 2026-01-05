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
├── .env.example
├── .gitignore
└── README.md

⚙️ Setup Instructions
1️⃣ Clone Repository
bashgit clone https://github.com/Achennar113/AI-Legal-Document-Analyzer-QA-Agent.git
cd AI-Legal-Document-Analyzer-QA-Agent
2️⃣ Create Virtual Environment
bashpython -m venv venv
Activate the virtual environment:

Windows:

bash  venv\Scripts\activate

macOS/Linux:

bash  source venv/bin/activate
3️⃣ Install Dependencies
bashpip install -r requirements.txt
4️⃣ Install Tesseract OCR (for scanned PDFs)

Windows: Download from Tesseract at UB Mannheim
macOS:

bash  brew install tesseract

Linux:

bash  sudo apt-get install tesseract-ocr
5️⃣ Environment Variables
Create a .env file in the root directory:
envGROQ_API_KEY=your_groq_api_key_here
⚠️ Security Note: Never commit .env to version control (already in .gitignore).
You can copy .env.example as a template:
bashcp .env.example .env

▶️ Run Backend (Django)
bashcd backend
python manage.py migrate
python manage.py runserver
Backend runs at: http://127.0.0.1:8000

▶️ Run Frontend (Streamlit)
Open a new terminal window:
bashcd frontend
streamlit run app.py
Frontend runs at: http://localhost:8501

🔌 API Endpoints
📥 Ingest Document
Endpoint: POST /api/ingest/
Request Body:
json{
  "text": "This contract may be terminated with 30 days notice."
}
Response:
json{
  "status": "success",
  "message": "Document ingested successfully",
  "chunks": 5
}
❓ Ask Question
Endpoint: POST /api/ask/
Request Body:
json{
  "query": "What is the termination clause?"
}
Response:
json{
  "answer": "The contract may be terminated with 30 days notice.",
  "sources": ["chunk_1", "chunk_3"]
}

📊 Example Use Cases

✅ Legal contract review
✅ Risk & compliance analysis
✅ Clause extraction
✅ Legal document summarization
✅ Law-tech / AI research demos


🛠️ Troubleshooting
Issue: Tesseract not found
Solution: Make sure Tesseract is installed and added to PATH.
Issue: GROQ_API_KEY error
Solution: Check that your .env file exists and contains a valid API key.
Issue: FAISS installation fails
Solution: Try installing with:
bashpip install faiss-cpu

🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository
Create a feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request


📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

👨‍💻 Author
Achennar113
GitHub: @Achennar113

🌟 Star this repo
If you find this project useful, please consider giving it a ⭐ on GitHub!

📧 Contact
For questions or support, please open an issue on GitHub or reach out via email.

Made with ❤️ using LangChain, FAISS, and Groq AIClaude is AI and can make mistakes. Please double-check responses.
