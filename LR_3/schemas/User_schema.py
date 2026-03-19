from pydantic import BaseModel, ConfigDict
from Currency_schema import CurrencyResponse

class UserCreate(BaseModel):
    username: str
    email: str

    model_config = ConfigDict(from_attributes=True)

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    currencies: list[CurrencyResponse]

    model_config = ConfigDict(from_attributes=True)