from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException

import models,schemas,crud
import database


###api_main
database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/ToDo/get_ToDo_all",response_model=List[schemas.ToDo])
async def read_ToDo_all(skip: int = 0, limit: int = 100, db:Session = Depends(get_db)):
    ToDos = crud.get_ToDo_all(db, skip=skip, limit=limit)
    return ToDos

@app.get("/ToDo/get_users_all",response_model=List[schemas.User])
async def read_ToDo_all(skip: int = 0, limit: int = 100, db:Session = Depends(get_db)):
    users = crud.get_user_all(db, skip=skip, limit=limit)
    return users

#defの引数はBasemodelを継承する必要がある
@app.post("/ToDo/get",response_model=schemas.ToDo)
async def read_ToDo(ToDo: schemas.ToDo_id, db:Session = Depends(get_db)):
    print(ToDo.ToDo_id)
    db_ToDo =  crud.get_ToDo(db=db, ToDo_id = ToDo.ToDo_id)
    if db_ToDo is None:
        raise HTTPException(status_code=404, detail="id not found")
    return db_ToDo

#postはBasemodelもしくはjsonで泣ければならない
@app.post("/ToDo/create_ToDo", response_model=schemas.ToDo)
async def creates_ToDo(ToDo : schemas.ToDoCreate, db: Session = Depends(get_db)):
    return crud.create_ToDo(db=db, ToDo=ToDo)

#postはBasemodelもしくはjsonで泣ければならない
@app.post("/ToDo/create_user", response_model=schemas.User)
async def creates_ToDo(user : schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@app.post("/ToDo/delete", response_model=schemas.ToDo)
async def deletes_ToDo(ToDo: schemas.ToDo_id, db: Session = Depends(get_db)):
    db_ToDo =  crud.delete_ToDo(db=db, ToDo_id = ToDo.ToDo_id)
    if db_ToDo is None:
        raise HTTPException(status_code=404, detail="id not found")
    return db_ToDo

@app.post("/ToDo/update", response_model=schemas.ToDo)
async def deletes_ToDo(ToDo: schemas.update, db: Session = Depends(get_db)):
    print(ToDo.ToDo_id, ToDo.description)
    db_ToDo =  crud.update_ToDo(db=db, ToDo_id = ToDo.ToDo_id, description = ToDo.description)
    if db_ToDo is None:
        raise HTTPException(status_code=404, detail="id not found")
    return db_ToDo