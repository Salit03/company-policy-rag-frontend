# Company Policy Assistant — RAG Application

A simple AI-powered application that answers questions about a company policy document. Instead of searching through a long PDF manually, users can ask questions in plain English and get answers based on the document.

I built this project to understand how Retrieval-Augmented Generation (RAG) works and how to connect a Python frontend with a deployed backend API.

## What it does

- Lets users ask questions about company policies through a chat interface.
- Retrieves relevant information from the policy document using semantic search.
- Uses Gemini to generate answers based on the retrieved context.
- Returns a fallback response when the available policy information is insufficient.
- Connects a Streamlit frontend to a FastAPI backend.

## Tech Stack

- **Python** — application logic
- **Streamlit** — frontend and chat interface
- **Requests** — communication with the backend API
- **FastAPI** — backend REST API
- **Gemini** — answer generation and embeddings
- **ChromaDB** — vector storage and similarity search
- **Docker** — backend containerization
- **Render** — backend deployment

## How it works

1. The company policy PDF is loaded and its text is extracted.
2. The text is divided into smaller chunks.
3. Each chunk is converted into an embedding.
4. The embeddings