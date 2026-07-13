from fastapi import APIRouter
from backend.app.data_loader import df

router = APIRouter()

@router.get("/recommend")
def recommend(category: str):
    result = df[
        df["Category"].str.contains(category, case=False, na=False)
    ]

    return result.to_dict(orient="records")