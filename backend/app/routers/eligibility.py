from fastapi import APIRouter
from backend.app.schemes.profile_scheme import UserProfile
from backend.app.services.eligibility_service import check_eligibility

router = APIRouter(prefix="/eligibility", tags=["Eligibility"])

@router.post("/")
def eligibility(profile: UserProfile):
    schemes = check_eligibility(profile)

    return {
        "eligible": len(schemes) > 0,
        "count": len(schemes),
        "schemes": schemes
    }