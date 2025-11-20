import httpx
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

LOCAL_API_URL = "http://host.docker.internal:11434/api/chat"
system = "U are AI assistant"

class GenerateRequest(BaseModel):
    promt: str

class AnswerResponse(BaseModel):
    text: str

@app.post("/generate_text")
async def generate_text(req: GenerateRequest) -> AnswerResponse:
    prompt = req.promt

    conversation = [
        {"role": "user", "content": prompt}
    ]

    payload = {
        "model": "qwen2:0.5b",
        "messages": conversation,
        "stream": False
    }

    headers = {"Content-Type": "application/json"}

    response = httpx.post(LOCAL_API_URL, json=payload, headers=headers, timeout=120)
    response.raise_for_status()  # чтобы выбросить ошибку, если что-то не так

    return AnswerResponse(text=response.content)
