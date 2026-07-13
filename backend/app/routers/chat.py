from fastapi import APIRouter
from backend.app.data_loader import df

router = APIRouter()

@router.get("/search")
def search_scheme(query: str):
    result = df[
        df["Scheme Name"].str.contains(query, case=False, na=False)
        | df["Keywords"].str.contains(query, case=False, na=False)
        | df["Category"].str.contains(query, case=False, na=False)
    ]

    return result.to_dict(orient="records")