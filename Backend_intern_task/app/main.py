from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def read_root(db: Session = Depends(database.get_db)):
    users = crud.get_all_users(db)  # Fetch users from the database
    return {"users": users}  # Return user information

@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return crud.create_user(db=db, user=user)

@app.post("/expenses/", response_model=schemas.ExpenseResponse)
def create_expense(expense: schemas.ExpenseCreate, user_id: int, db: Session = Depends(database.get_db)):
    return crud.create_expense(db=db, expense=expense, user_id=user_id)

@app.get("/users/{user_id}/expenses/")
def get_user_expenses(user_id: int, db: Session = Depends(database.get_db)):
    return crud.get_expenses_by_user(db=db, user_id=user_id)
