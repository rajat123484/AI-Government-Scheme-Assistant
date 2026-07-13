from fastapi import APIRouter
from backend.app.schemas.profile_schema import Profile

router = APIRouter()

profile = {}

@router.post("/profile")
def save_profile(data: Profile):
    global profile
    profile = data.model_dump()   # Convert Pydantic model to dict
    return {
        "message": "Profile saved",
        "profile": profile
    }

@router.get("/profile")
def get_profile():
    return profile