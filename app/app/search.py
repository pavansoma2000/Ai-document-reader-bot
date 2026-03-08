from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from ollama import Client

ollama = Client(host="http://ollama:11434")

embeddings = HuggingFaceEmbeddings()

db = Chroma(
    persist_directory="vectordb",
    embedding_function=embeddings
)

def ask_bot(query):

    docs = db.similarity_search(query, k=2)

    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
Answer ONLY using the context below.

Context:
{context}

Question:
{query}
"""

    response = ollama.chat(
        model="tinyllama",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"], docs
