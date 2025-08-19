from fastapi import HTTPException, Header
import os

SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
ALGORITHM = "HS256"

async def verify_api_key(x_api_key: str = Header(...)):
    """Verify API key authentication"""
    valid_api_key = os.getenv("API_KEY", "default-api-key")
    
    if x_api_key != valid_api_key:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )
    return x_api_key