from pydantic import BaseModel

class UserProfile(BaseModel):
    age: int
    gender: str
    state: str
    income: float
    category: str
    occupation: str