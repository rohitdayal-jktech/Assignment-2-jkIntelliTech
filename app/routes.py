from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from . import crud, schemas, database, auth

router = APIRouter()

@router.get("/")
def read_root():
    return JSONResponse(
        content={"message": "Welcome to the ToDo List API. Visit /docs for API documentation."}
    )

@router.post("/register", response_model=schemas.UserResponse)
def register_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = auth.get_user(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return auth.create_user(db, user)

@router.post("/login", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/todos/", response_model=schemas.ToDoResponse)
def create(todo: schemas.ToDoCreate, db: Session = Depends(database.get_db), current_user: schemas.UserResponse = Depends(auth.get_current_user)):
    return crud.create_todo(db, todo)

@router.get("/todos/", response_model=list[schemas.ToDoResponse])
def read_all(db: Session = Depends(database.get_db), current_user: schemas.UserResponse = Depends(auth.get_current_user)):
    return crud.get_todos(db)

@router.get("/todos/{todo_id}", response_model=schemas.ToDoResponse)
def read(todo_id: int, db: Session = Depends(database.get_db), current_user: schemas.UserResponse = Depends(auth.get_current_user)):
    todo = crud.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.put("/todos/{todo_id}", response_model=schemas.ToDoResponse)
def update(todo_id: int, todo: schemas.ToDoUpdate, db: Session = Depends(database.get_db), current_user: schemas.UserResponse = Depends(auth.get_current_user)):
    updated = crud.update_todo(db, todo_id, todo)
    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated

@router.delete("/todos/{todo_id}")
def delete(todo_id: int, db: Session = Depends(database.get_db), current_user: schemas.UserResponse = Depends(auth.get_current_user)):
    deleted = crud.delete_todo(db, todo_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"detail": "Deleted"}