import os
import requests
import streamlit as st

DEFAULT_API_URL = "https://company-policy-rag-52nq.onrender.com"

st.set_page_config(
    page_title="Company Policy Assistant",
    page_icon="📘",
    layout="centered",
)

st.markdown(
    """
    <style>
      .block-container {max-width: 900px; padding-top: 2.2rem; padding-bottom: 2rem;}
      .hero {
        padding: 1.5rem 1.6rem;
        border-radius: 18px;
        background: linear-gradient(135deg, #152b4a 0%, #28618a 100%);
        color: white;
        margin-bottom: 1.25rem;
      }
      .hero h1 {color: white; margin-bottom: .35rem; font-size: 2rem;}
      .hero p {color: #e7f1fb; margin-bottom: 0;}
      .small-note {color: #6b7280; font-size: .88rem;}
      div[data-testid="stChatMessage"] {border-radius: 14px;}
      .stButton button {border-radius: 10px;}
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.header("⚙️ Settings")
    api_url = st.text_input(
        "Backend API URL",
        value=os.getenv("RAG_API_URL", DEFAULT_API_URL),
        help="Your deployed FastAPI service URL, without /ask at the end.",
    ).strip().rstrip("/")
    st.caption("This frontend sends your question to the FastAPI /ask endpoint.")
    if st.button("Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.divider()
    st.markdown("**Powered by**")
    st.write("Gemini · ChromaDB · FastAPI")
    st.caption("Only ask questions about the policy document connected to this backend.")

st.markdown(
    """
    <div class="hero">
      <h1>📘 Company Policy Assistant</h1>
      <p>Ask a question in plain English and get an answer grounded in the company policy document.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.info("Example: “How long must an employee work before they can request personal leave?”")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask a question about company policy…")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        if not api_url:
            answer = "Please enter your backend API URL in Settings."
            st.warning(answer)
        else:
            try:
                with st.spinner("Searching the policy and preparing an answer…"):
                    response = requests.post(
                        f"{api_url}/ask",
                        json={"question": question},
                        timeout=120,
                    )
                if response.ok:
                    data = response.json()
                    answer = data.get("answer", "The API returned no answer.")
                    st.markdown(answer)
                else:
                    answer = (
                        f"The API returned HTTP {response.status_code}. "
                        "Please try again in a moment."
                    )
                    st.error(answer)
                    with st.expander("Technical details"):
                        st.code(response.text[:2000])
            except requests.exceptions.Timeout:
                answer = "The request took too long. The backend may be waking up; please try again."
                st.warning(answer)
            except requests.exceptions.RequestException as exc:
                answer = "Could not connect to the backend. Check the API URL and try again."
                st.error(answer)
                with st.expander("Technical details"):
                    st.code(str(exc))

    st.session_state.messages.append({"role": "assistant", "content": answer})

st.divider()
st.markdown(
    '<p class="small-note">Demo application · Answers are generated from the connected policy knowledge base. '
    'Always verify important HR decisions against the official policy.</p>',
    unsafe_allow_html=True,
)
