from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    email: str
    cpf: str
    phone: str
    address: str
    profession: str
    description: str

class UserRequest(User):
    ...

class UserResponse(User):
    id: int

    class Config:
        from_attributes=True
        orm_mode = True