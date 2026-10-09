# Company Policy Assistant — Frontend

A simple Streamlit chat UI connected to the deployed FastAPI RAG backend.

## Technology used

- **Streamlit**: builds the user interface in Python; no separate HTML/CSS/React setup needed.
- **Requests**: sends the user's question to the FastAPI backend.
- **FastAPI backend**: `https://company-policy-rag-52nq.onrender.com`
- The frontend calls `POST /ask` with JSON: `{"question": "..."}`.

## Run locally on your Mac

1. Download and unzip this folder.
2. Open the folder in VS Code.
3. Open the terminal in this folder.
4. (Recommended) create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
5. Install packages:
   ```bash
   python -m pip install -r requirements.txt
   ```
6. Start the frontend:
   ```bash
   streamlit run app.py
   ```
7. Open the local URL Streamlit shows, usually `http://localhost:8501`.

The backend URL is already set to the deployed API. You do not need to put the Gemini API key in the frontend; the key stays in the backend's Render environment variables.

## Deploy the frontend

Push these frontend files to a GitHub repository, then create a Streamlit Community Cloud app from that repository, selecting `app.py` as the main file. If you use another host, set the start command to `streamlit run app.py --server.address 0.0.0.0 --server.port $PORT` if required by that host.

## Important

- Do not add your Gemini API key to this frontend or commit it to GitHub.
- The frontend is a chat interface only. The RAG logic, embeddings, ChromaDB, and Gemini calls remain in the backend.
