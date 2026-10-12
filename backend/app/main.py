from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Medical Consultant API", version="0.1.0")

RED_FLAGS = {"胸痛", "呼吸困难", "大出血", "意识不清", "昏迷", "抽搐"}

class ChatRequest(BaseModel):
    message: str
    history: list[dict[str, str]] = []

class ChatResponse(BaseModel):
    reply: str
    urgent: bool
    sources: list[str] = []

@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    urgent = any(term in request.message for term in RED_FLAGS)
    if urgent:
        reply = "你描述的症状可能属于紧急情况。请立即拨打当地急救电话或前往最近的急诊科，不要等待线上回复。"
    else:
        reply = "我已记录你的描述。为了提供更有帮助的健康信息，请补充症状持续时间、严重程度、年龄和既往病史。"
    return ChatResponse(reply=reply, urgent=urgent, sources=["demo-safety-policy"])
