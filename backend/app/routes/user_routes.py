from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database import get_db

from app.models.user import User
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

router = APIRouter()


@router.post("/users")
def create_user(user_data: UserCreate, db:Session = Depends(get_db)):
    user = User(
        name=user_data.name,
        email=user_data.email
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get("/users",)
def get_users(db:Session = Depends(get_db)):
    return db.query(User).all()

@router.get("/users/{id}")
def get_user(id:int,db:Session = Depends(get_db)):
    return db.query(User).filter(User.id == id).first()

@router.delete("/users/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}