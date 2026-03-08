import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

DOC_PATH = "docs"
DB_PATH = "vectordb"


def load_documents():

    documents = []

    for file in os.listdir(DOC_PATH):

        if file.endswith(".pdf"):

            loader = PyPDFLoader(os.path.join(DOC_PATH, file))
            pages = loader.load()

            for page in pages:
                page.metadata["source"] = file

            documents.extend(pages)

    return documents


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    return splitter.split_documents(documents)


def create_vector_db(chunks):

    embeddings = HuggingFaceEmbeddings()

    db = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=DB_PATH
    )

    db.persist()


if __name__ == "__main__":

    print("Loading documents...")
    docs = load_documents()

    print("Splitting documents...")
    chunks = split_documents(docs)

    print("Creating vector database...")
    create_vector_db(chunks)

    print("Ingestion completed!")
