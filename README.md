# Ai-document-reader-bot

The AI Document Search Bot is an intelligent document assistant that allows users to search and retrieve information from a centralized document repository. The system uses AI-powered semantic search and retrieval techniques to find relevant information from stored documents and generate answers strictly based on the content of those documents.

Unlike traditional keyword-based search systems, this bot uses vector embeddings and Retrieval-Augmented Generation (RAG) to understand the meaning of user queries and return accurate results along with the original document sources.

Key Features
1. Centralized Document Repository

All documents are stored in a single location, making it easy to manage and search organizational knowledge.

2. AI-Powered Semantic Search

The bot converts documents into vector embeddings and stores them in a vector database (ChromaDB).
This allows the system to search documents based on meaning rather than exact keywords.

3. Document-Based Answers

The bot generates responses only from the content available in the documents.
It does not generate its own information, which helps ensure accuracy and reliability.

4. Source References
Each answer includes:
* Document name
* Page reference (when available)
* A clickable source to open the original document
* This allows users to verify the information directly from the source.

5. Interactive Web Interface
The system provides a simple Streamlit-based user interface where users can:
* Enter search queries
* View AI-generated answers
* Access the original documents

6. Containerized Deployment
The entire system runs inside Docker containers, making it easy to deploy and manage across environments.

System Architecture

The bot follows a Retrieval-Augmented Generation (RAG) architecture.

Workflow:

Documents are uploaded to the system.

The ingestion pipeline processes documents and splits them into smaller chunks.

Each chunk is converted into embeddings using an embedding model.

Embeddings are stored in Chroma Vector Database.

When a user asks a question:

The system performs a semantic search in the vector database.

Relevant document chunks are retrieved.

The AI model generates an answer using only the retrieved content.

The system returns the answer along with the document sources.

Technologies Used

Programming Language

Python

AI / NLP

LangChain

Ollama

TinyLlama / Phi3 models

Vector Database

ChromaDB

Document Processing

PyPDFLoader

Text Splitters

Frontend

Streamlit

Containerization

Docker

Docker Compose

Use Cases

This system can be used for:

Internal knowledge base search

Technical documentation assistant

Company policy document search

DevOps runbook lookup

Research document exploration

SharePoint-like AI document assistant

Benefits

Faster information retrieval

Improved knowledge accessibility

Reduced manual document searching

Accurate answers with verifiable sources

Scalable AI-powered document management
