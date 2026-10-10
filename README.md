# Company Policy Assistant — RAG Application

An AI-powered application that allows users to ask questions about a company policy document in plain English and receive answers grounded in the document.

This project was built to understand Retrieval-Augmented Generation (RAG) and integrate a Streamlit frontend with a deployed FastAPI backend.

## Live Demo

- **Frontend Application:** https://company-policy-rag-frontend.onrender.com
- **Backend API:** https://company-policy-rag-52nq.onrender.com/
- **API Documentation (Swagger UI):** https://company-policy-rag-52nq.onrender.com/docs

## Source Code

- **Frontend Repository:** https://github.com/Salit03/company-policy-rag-frontend
- **Backend Repository:** https://github.com/Salit03/genai-rag-project

## What It Does

- Allows users to ask questions about company policies through a chat interface.
- Retrieves relevant information from the policy document using semantic search.
- Uses Google's Gemini model to generate answers based on retrieved context.
- Returns a fallback response when the available policy information is insufficient.
- Connects a Streamlit frontend to a deployed FastAPI backend.
- Displays responses in a simple conversational interface.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Frontend and chat interface |
| Requests | Communication with the backend API |
| FastAPI | Backend REST API |
| Google Gemini | Answer generation and embeddings |
| ChromaDB | Vector storage and similarity search |
| LangChain Text Splitters | Document chunking |
| Docker | Frontend containerization |
| Render | Cloud deployment |

## How It Works

1. **Document Loading:** The backend loads the company policy PDF and extracts its text.
2. **Text Chunking:** The extracted text is divided into smaller chunks.
3. **Embedding Generation:** Each chunk is converted into a numerical embedding.
4. **Vector Storage:** The embeddings and associated text are stored in ChromaDB.
5. **User Query:** The user enters a question through the Streamlit chat interface.
6. **API Request:** The frontend sends the question to the backend's `/ask` endpoint.
7. **Semantic Retrieval:** The backend searches ChromaDB for relevant document chunks.
8. **Answer Generation:** Gemini generates an answer using the retrieved context.
9. **Response Display:** The backend returns a JSON response, and the frontend displays the answer.

## Architecture

```text
User
 |
 v
Streamlit Frontend
 |
 | HTTP POST /ask
 v
FastAPI Backend
 |
 v
Query Embedding
 |
 v
ChromaDB Similarity Search
 |
 v
Relevant Document Chunks
 |
 v
Context + User Question
 |
 v
Google Gemini
 |
 v
Generated Answer
 |
 v
Streamlit Chat Interface
```

## Backend API

The frontend communicates with the backend using the following endpoint:

`POST /ask`

### Example Request

```json
{
  "question": "How long must an employee work before they can request personal leave?"
}
```

### Example Response

```json
{
  "question": "How long must an employee work before they can request personal leave?",
  "answer": "An employee must have completed at least 12 months of service to request personal leave."
}
```

For interactive testing, visit the [Swagger API Documentation](https://company-policy-rag-52nq.onrender.com/docs).

## Local Setup

### Prerequisites

- Python 3.10 or later
- Git
- Access to the deployed backend API, or a locally running backend

### 1. Clone the Repository

```bash
git clone https://github.com/Salit03/company-policy-rag-frontend.git
cd company-policy-rag-frontend
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Frontend

```bash
streamlit run app.py
```

Open the local application at:

http://localhost:8501

### 5. Configure the Backend API URL

The frontend uses the deployed backend by default. If the application provides a Backend API URL setting in the sidebar, you can use it to specify a different backend URL.

For a local backend, use:

`http://localhost:8000`

Make sure the backend is running before sending questions.

## Deployment

The frontend is deployed on Render as a Docker-based service and communicates with the separately deployed FastAPI backend.

- **Frontend hosting:** Render
- **Frontend runtime:** Docker
- **Backend hosting:** Render
- **Backend framework:** FastAPI

### Deployment Notes

- Free-tier Render services may spin down after inactivity, making the first request slower.
- Temporary `502 Bad Gateway` errors may occur if the backend is unavailable or takes too long to respond.
- The frontend depends on the backend API being reachable.
- The backend must have a valid `GEMINI_API_KEY` configured in its environment settings.
- The backend's ChromaDB storage must remain available for retrieval to work correctly.

## Future Improvements

- Support uploading multiple PDF documents.
- Allow users to select which documents to query.
- Display source citations with generated answers.
- Improve error handling and user-facing status messages.
- Add chat history management and conversation export.
- Improve backend availability and persistent vector storage.
- Add automated tests and application monitoring.

## Learning Outcomes

- Understanding the RAG application workflow
- Integrating a Python frontend with a REST API
- Working with Streamlit and FastAPI
- Understanding embeddings, semantic search, and vector databases
- Connecting an LLM to retrieved document context
- Containerizing and deploying an application using Docker and Render

---

**Author:** Salit Kumar
