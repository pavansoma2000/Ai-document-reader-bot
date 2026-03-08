import streamlit as st
import os

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from ollama import Client

ollama = Client(host="http://ollama:11434")

DB_PATH = "vectordb"
DOC_PATH = "docs"

embeddings = HuggingFaceEmbeddings()

db = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embeddings
)

st.title("📄 AI Document Search Bot")

query = st.text_input("Ask something about your documents")

if query:

    docs = db.similarity_search(query, k=2)

    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
Answer ONLY using the information in the context below.

Context:
{context}

Question:
{query}
"""

    response = ollama.chat(
        model="tinyllama",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response["message"]["content"]

    st.subheader("Answer")
    st.write(answer)

st.subheader("Sources")

for doc in documents:

    source = doc.metadata.get("source")

    filename = os.path.basename(source)

    filepath = os.path.join(DOC_PATH, filename)

    st.write(f"📄 {filename}")

    if os.path.exists(filepath):

        with open(filepath, "rb") as f:
            st.download_button(
                label="Open Document",
                data=f,
                file_name=filename
            )

    else:
        st.write("File not found:", filepath)
