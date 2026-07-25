from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.routers import (
    profile,
    recommendation,
    chat,
    eligibility,
    checklist
)

app = FastAPI(
    title="AI Government Scheme Assistant",
    description="Backend API for AI-powered Government Scheme Recommendation System",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Routers
app.include_router(profile.router)
app.include_router(recommendation.router)
app.include_router(chat.router)
app.include_router(eligibility.router)
app.include_router(checklist.router)

@app.get("/")
def home():
    return {
        "success": True,
        "message": "AI Government Scheme Assistant Backend Running 🚀",
        "version": "1.0.0"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "backend": "running"
    }