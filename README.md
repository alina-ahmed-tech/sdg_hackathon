Clone the Repo

```bash
git clone git@github.com:alina-ahmed-tech/sdg_hackathon.git
cd 
```

---

### LLM Setup (Ollama)

1. **Install Ollama**

   ```bash
   # Install via Homebrew cask
   brew install --cask ollama

   # Start the Ollama daemon
   ollama serve
   ```

2. **Pull & Run Mistral Small Instruct**

   ```bash
   ollama run 7shi/mistral-small:22b-instruct-2409-iq3_M
   ```

---

### Python Environment & API Server

1. **Create and activate a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies**

   ```bash
   pip install --upgrade pip
   pip install fastapi "uvicorn[standard]" streamlit requests langchain langchain-ollama ollama
   ```

3. **Run the FastAPI app**

   ```bash
   uvicorn app:app --reload --port 8002
   ```

   or, to explicitly use the venv’s interpreter:

   ```bash
   python -m uvicorn app:app --reload --port 8002
   ```
---

### Frontend UI (Streamlit)

1. **Run the Streamlit dashboard**

   ```bash
   streamlit run streamlit_app.py
   ```

2. **Use the UI**

   * Paste your training code in the text area
  
   ```bash
   for epoch in range(10): train(batch)
   ```
   * Enter GPU/CPU details.
   * Click **Get eco-tips** and view the recommendations.
