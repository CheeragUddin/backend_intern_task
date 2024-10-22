from pydantic import BaseModel
from typing import List

class UserCreate(BaseModel):
    name: str
    email: str
    mobile: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    mobile: str

    class Config:
        orm_mode = True

class ExpenseCreate(BaseModel):
    description: str
    total_amount: float
    split_method: str  # 'equal', 'exact', 'percentage'
    splits: List[dict]  # list of {'user_id': int, 'amount_owed': float}

class ExpenseResponse(BaseModel):
    id: int
    description: str
    total_amount: float
    split_method: str

    class Config:
        orm_mode = True
