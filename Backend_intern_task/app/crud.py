from sqlalchemy.orm import Session
from . import models, schemas


def get_all_users(db: Session):
    return db.query(models.User).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email, mobile=user.mobile)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_expense(db: Session, expense: schemas.ExpenseCreate, user_id: int):
    db_expense = models.Expense(description=expense.description, total_amount=expense.total_amount, split_method=expense.split_method, owner_id=user_id)
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    
    for split in expense.splits:
        db_split = models.ExpenseSplit(expense_id=db_expense.id, user_id=split["user_id"], amount_owed=split["amount_owed"])
        db.add(db_split)
    
    db.commit()
    return db_expense

def get_expenses_by_user(db: Session, user_id: int):
    return db.query(models.Expense).filter(models.Expense.owner_id == user_id).all()
