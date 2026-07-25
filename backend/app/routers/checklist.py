from fastapi import APIRouter

router = APIRouter(prefix="/checklist", tags=["Checklist"])

@router.get("/")
def checklist():
    return {
        "documents": [
            "Aadhaar Card",
            "Income Certificate",
            "Residence Certificate",
            "Bank Passbook",
            "Passport Size Photograph"
        ]
    }