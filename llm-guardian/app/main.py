from fastapi import FastAPI, HTTPException, Depends, Header
from pydantic import BaseModel
import uvicorn
from .models.classifier import PromptClassifier
from .api.auth import verify_api_key

app = FastAPI(
    title="LLM Guardian API - HS Aalen",
    description="Prompt injection detection and protection",
    version="1.0.0"
)

# Initialize classifier
classifier = PromptClassifier()

class PromptRequest(BaseModel):
    prompt: str

class PromptResponse(BaseModel):
    status: str  # "OK" or "BLOCKED"
    confidence: float

@app.post("/analyze", response_model=PromptResponse)
async def analyze_prompt(
    request: PromptRequest,
    api_key: str = Depends(verify_api_key) # hardcoded in env files
):
    try:
        result = classifier.classify(request.prompt)
        
        if result["is_malicious"]:
            return PromptResponse(
                status="BLOCKED",
                confidence=result["confidence"]
            )
        else:
            return PromptResponse(
                status="OK",
                confidence=result["confidence"]
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy", "model_loaded": classifier.is_loaded()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info", reload=True, workers=4)