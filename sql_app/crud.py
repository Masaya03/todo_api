from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode
import models, schemas, database
from fastapi import HTTPException
from database import Base
import datetime

###CRUD用
##modelsが実際は必要になる
def get_ToDo_all(db: Session, skip:int = 0, limit: int=100):
    return db.query(models.ToDo).offset(skip).limit(limit).all()

def get_user_all(db: Session, skip:int = 0, limit: int=100):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_ToDo(db:Session, ToDo_id: int):
    return db.query(models.ToDo).filter(models.ToDo.ToDo_id == ToDo_id).first()

def get_user(db:Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def create_ToDo(db: Session, ToDo: schemas.ToDo):
    ToDo_obj = get_user(db=db,user_id = ToDo.user_id)
    if ToDo_obj is not None:
        print("query is valid")
        db_ToDo = models.ToDo(user_id=ToDo.user_id,description = ToDo.description,due_date = ToDo.due_date
        ,reg_date = datetime.datetime.today())
        db.add(db_ToDo)
        db.commit()
        db.refresh(db_ToDo)
        return db_ToDo

def create_user(db: Session, user: schemas.User):
    db_user = models.User(username=user.username)

#    db_ToDo = database.models.ToDo(description=ToDo.description)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_ToDo(db: Session, ToDo_id: int , description: str):
    ToDo_obj = get_ToDo(db=db,ToDo_id=ToDo_id)
    if ToDo_obj is not None:
        print("query is valid")
        ToDo_obj.description = description
        db.commit()
    return ToDo_obj

def delete_ToDo(db: Session, ToDo_id:int):
    ToDo_obj = get_ToDo(db=db,ToDo_id=ToDo_id)
    if ToDo_obj is not None:
        db.delete(ToDo_obj)
        db.commit()
    return ToDo_obj
