from fastapi import APIRouter
from app.schemas.profile_schema import UserProfile
from app.services.eligibility_service import check_eligibility

router = APIRouter()

@router.post("/profile")
def create_profile(profile: UserProfile):

    schemes = check_eligibility(profile)

    return {
        "message": "Profile received successfully!",
        "profile": profile,
        "eligible_schemes": schemes
    }