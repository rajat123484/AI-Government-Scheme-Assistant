from fastapi import FastAPI
from app.routers import profile
app = FastAPI(
    title="AI Government Scheme Assistant",
    version="1.0.0"
)
app.include_router(profile.router)
@app.get("/")
def home():
    return {
        "message": "AI Government Scheme Assistant Backend Running 🚀"
    }