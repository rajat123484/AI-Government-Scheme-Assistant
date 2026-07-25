from fastapi import APIRouter
from backend.app.schemes.profile_scheme import UserProfile
from backend.app.services.recommendation_service import get_recommendations

router = APIRouter(
    prefix="/recommendation",
    tags=["Recommendation"]
)


@router.post("/")
def recommendation(profile: UserProfile):

    result = get_recommendations(profile)

    return {
        "success": True,
        "message": "Recommendation generated successfully.",
        "data": result
    }