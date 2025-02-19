from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
import torch

app = FastAPI(title="Condense Notebook")

summarizer = pipeline(
    "summarization",
    model="deepseek-ai/deepseek-llm-7b-base",
    device=0 if torch.cuda.is_available() else -1
)

class SummarizationRequest(BaseModel):
    text: str
    max_length: int = 130
    min_length: int = 30

class SummarizationResponse(BaseModel):
    summary: str

@app.post("/summarize", response_model=SummarizationResponse)
async def summarize_text(request: SummarizationRequest):
    try:
        # Generate summary
        summary = summarizer(
            request.text,
            max_length=request.max_length,
            min_length=request.min_length,
            do_sample=False
        )[0]['summary_text']
        
        return SummarizationResponse(summary=summary)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
