from pydantic import BaseModel
from typing import Optional

class ToDoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class ToDoCreate(ToDoBase):
    pass

class ToDoUpdate(ToDoBase):
    pass

class ToDoResponse(ToDoBase):
    id: int

    class Config:
        from_attributes = True  # Tells Pydantic to convert SQLAlchemy to Pydantic

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None