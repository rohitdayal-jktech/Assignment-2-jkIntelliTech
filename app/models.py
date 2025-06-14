from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class ToDo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255))
    completed = Column(Boolean, default=False)
