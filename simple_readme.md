# 🧠 AI Legal Document Analyzer

> Intelligent legal document analysis powered by AI - Extract insights, answer questions, and identify risks instantly.

## ✨ What It Does

Upload any legal document and get instant answers to your questions. Our AI analyzes contracts, agreements, and legal texts to help you understand key clauses, risks, and obligations.

## 🎯 Key Features

- **Smart Document Upload** - Support for PDF, TXT, and scanned documents
- **Instant Q&A** - Ask questions and get accurate answers from your documents
- **Risk Detection** - Automatically identify potential legal risks
- **Clause Extraction** - Find specific clauses and terms quickly
- **OCR Support** - Works with scanned and image-based PDFs

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Tesseract OCR ([Download here](https://github.com/UB-Mannheim/tesseract/wiki))

### Installation

```bash
# Clone the repository
git clone https://github.com/Achennar113/AI-Legal-Document-Analyzer-QA-Agent.git
cd AI-Legal-Document-Analyzer-QA-Agent

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your GROQ_API_KEY to .env file
```

### Running the Application

**Start Backend:**
```bash
cd backend
python manage.py migrate
python manage.py runserver
```

**Start Frontend** (in a new terminal):
```bash
cd frontend
streamlit run app.py
```

Visit `http://localhost:8501` to use the application!

## 💡 How to Use

1. **Upload** your legal document (PDF or TXT)
2. **Wait** for the AI to process and analyze it
3. **Ask** any questions about the document
4. **Get** instant, accurate answers with source references

## 🛠️ Built With

- **Frontend:** Streamlit
- **Backend:** Django REST Framework
- **AI Engine:** LangChain + Groq LLaMA
- **Vector Database:** FAISS
- **OCR:** Tesseract + OpenCV

## 📸 Screenshots

*Coming soon - Upload your legal documents and see the magic happen!*

## 🤝 Contributing

We welcome contributions! Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests

## 📄 License

MIT License - feel free to use this project however you'd like!

## 💬 Support

Found a bug or have a question? [Open an issue](https://github.com/Achennar113/AI-Legal-Document-Analyzer-QA-Agent/issues)

---

⭐ **Star this repo** if you find it useful!

Made with ❤️ by [Achennar113](https://github.com/Achennar113)