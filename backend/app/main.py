from fastapi import FastAPI
from backend.app.data_loader import get_all_schemes
from backend.app.routers.chat import router as chat_router
from backend.app.routers.recommendation import router as recommendation_router
from backend.app.routers.eligibility import router as eligibility_router
from backend.app.routers.checklist import router as checklist_router
from backend.app.routers.profile import router as profile_router


app = FastAPI(
    title="AI Government Scheme Assistant",
    version="1.0.0"
)

app.include_router(chat_router)
app.include_router(recommendation_router)
app.include_router(eligibility_router)
app.include_router(checklist_router)
app.include_router(profile_router)

@app.get("/")
def home():
    return {
        "message": "AI Government Scheme Assistant Backend Running 🚀"
    }

@app.get("/schemes")
def schemes():
    return get_all_schemes()