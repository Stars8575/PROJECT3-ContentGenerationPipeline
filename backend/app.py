from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from pipeline import generate_content_pipeline

app = FastAPI(
    title="Content Generation Pipeline",
    version="1.0.0"
)

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ContentRequest(BaseModel):
    topic: str
    content_type: str
    tone: str
    word_count: int


@app.get("/")
def home():
    return {
        "message": "Content Generation Pipeline API",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/generate")
def generate(request: ContentRequest):

    result = generate_content_pipeline(
        topic=request.topic,
        content_type=request.content_type,
        tone=request.tone,
        word_count=request.word_count
    )

    return result