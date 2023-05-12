from datetime import datetime

from pydantic import BaseModel


class Operation(BaseModel):
    id: int
    quantity: str
    figi: str
    date: datetime
    instrument_type: str
    type: str

    class Config:
        orm_mode = True

class OperationCreate(BaseModel):
    id: int
    quantity: str
    figi: str
    instrument_type: str
    date: datetime
    type: str