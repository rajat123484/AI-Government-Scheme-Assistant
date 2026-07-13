from fastapi import APIRouter
from backend.app.data_loader import df

router = APIRouter()

@router.get("/documents")
def documents(scheme: str):
    result = df[
        df["Scheme Name"].str.contains(scheme, case=False, na=False)
    ][["Scheme Name", "Required Documents"]]

    return result.to_dict(orient="records")