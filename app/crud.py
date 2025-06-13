from sqlalchemy.orm import Session
from . import models, schemas

def get_todos(db: Session):
    return db.query(models.ToDo).all()

def get_todo(db: Session, todo_id: int):
    return db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()

def create_todo(db: Session, todo: schemas.ToDoCreate):
    db_todo = models.ToDo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, todo_id: int, new_data: schemas.ToDoUpdate):
    todo = get_todo(db, todo_id)
    if todo:
        for key, value in new_data.dict().items():
            setattr(todo, key, value)
        db.commit()
        db.refresh(todo)
    return todo

def delete_todo(db: Session, todo_id: int):
    todo = get_todo(db, todo_id)
    if todo:
        db.delete(todo)
        db.commit()
    return todo
