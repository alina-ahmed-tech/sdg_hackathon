https://github.com/user-attachments/assets/dd8f2815-a641-4adc-996f-10ee6df40029


<img width="1713" alt="crumbly_ss" src="https://github.com/user-attachments/assets/fafa218d-1ef1-473a-ba8a-d57c730cfa81" />


<h1> Skills: Python, FastAPI, HTTP & REST, LangChain, Prompt Engineering, Ollama (local LLM serving) </h1>

How it Works: 

* The user pastes their training code and enters GPU/CPU details in the Streamlit front-end.
* When the user clicks “Get eco-tips,” a HTTP POST request is sent to the FastAPI server, with a JSON body containing the code and hardware info.
* FastAPI server back-end receives the request and invokes LangChain’s OllamaLLM wrapper.
* LangChain formats the prompt template and sends it over HTTP to the local Ollama daemon running Mistral Small Instruct.
* Ollama returns the generated text which is three energy-saving tips.
* FastAPI packages that text into a JSON object and sends it back as the response to the original POST.
* Streamlit front-end receives the JSON, extracts the "recommendations" field, and renders it live in the browser displaying the result. 

---
<h1> Project setup </h1>

### Clone the Repo

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
