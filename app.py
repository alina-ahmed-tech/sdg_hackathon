from fastapi import FastAPI
from pydantic import BaseModel
from langchain_ollama.llms import OllamaLLM

class Req(BaseModel):
    code: str
    hardware: dict

app = FastAPI()

llm = OllamaLLM(model="7shi/mistral-small:22b-instruct-2409-iq3_M")

@app.post("/recommend")
def recommend(req: Req):
    prompt = f"""You are an AI efficiency coach. Given this training script:
{req.code}

And this hardware:
{req.hardware}

Suggest 3 changes (e.g. epochs, batch size, mixed precision…) to reduce energy use without major accuracy loss."""
    recs = llm.predict(prompt)
    return {"recommendations": recs}
