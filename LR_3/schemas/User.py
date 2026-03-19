from pydantic import BaseModel, Field
from Currency import CurrencyResponse

class UserCreate(BaseModel):
    username: str
    email: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    currencies: list[CurrencyResponse]