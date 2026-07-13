from fastapi import APIRouter
from backend.app.data_loader import df

router = APIRouter()

@router.get("/eligibility")
def eligibility(keyword: str):
    result = df[
        df["Eligibility"].str.contains(keyword, case=False, na=False)
    ]

    return result.to_dict(orient="records")