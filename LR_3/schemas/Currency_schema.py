from pydantic import BaseModel, ConfigDict

class CurrencyResponse(BaseModel):
    code: str
    name: str

    model_config = ConfigDict(from_attributes=True)