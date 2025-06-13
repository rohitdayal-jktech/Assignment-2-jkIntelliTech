from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas, database

router = APIRouter()

@router.post("/todos/", response_model=schemas.ToDoResponse)
def create(todo: schemas.ToDoCreate, db: Session = Depends(database.get_db)):
    return crud.create_todo(db, todo)

@router.get("/todos/", response_model=list[schemas.ToDoResponse])
def read_all(db: Session = Depends(database.get_db)):
    return crud.get_todos(db)

@router.get("/todos/{todo_id}", response_model=schemas.ToDoResponse)
def read(todo_id: int, db: Session = Depends(database.get_db)):
    todo = crud.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.put("/todos/{todo_id}", response_model=schemas.ToDoResponse)
def update(todo_id: int, todo: schemas.ToDoUpdate, db: Session = Depends(database.get_db)):
    updated = crud.update_todo(db, todo_id, todo)
    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated

@router.delete("/todos/{todo_id}")
def delete(todo_id: int, db: Session = Depends(database.get_db)):
    deleted = crud.delete_todo(db, todo_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"detail": "Deleted"}