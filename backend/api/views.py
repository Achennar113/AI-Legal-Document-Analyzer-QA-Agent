from rest_framework.decorators import api_view
from rest_framework.response import Response
from dotenv import load_dotenv

from langchain.schema import Document
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq

load_dotenv()

vectorstore = None

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

@api_view(["POST"])
def ingest_document(request):
    global vectorstore
    text = request.data.get("text")

    if not text:
        return Response({"error": "No text provided"}, status=400)

    documents = [Document(page_content=text)]
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(documents)

    vectorstore = FAISS.from_documents(chunks, embeddings)

    return Response({
        "status": "Document indexed",
        "chunks": len(chunks)
    })


@api_view(["POST"])
def ask_question(request):
    global vectorstore
    query = request.data.get("query")

    if vectorstore is None:
        return Response({"error": "No document indexed"}, status=400)

    docs = vectorstore.similarity_search(query, k=4)
    context = "\n\n".join(d.page_content for d in docs)

    prompt = f"""
Answer ONLY from the context.
If not found, say "Not found in document".

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)

    return Response({"answer": response.content})
