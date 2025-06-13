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
        orm_mode = True  # Tells Pydantic to convert SQLAlchemy to Pydantic
