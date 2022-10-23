#入れわすれ注意　orm_mode 辞書で
from sqlalchemy.sql.functions import mode
import datetime
from pydantic import BaseModel, Field
from typing import Optional

######FastAPIで使用するモデル SCHEMAS#######
class ToDoCreate(BaseModel):
    user_id: int
    description: str = Field(max_lenght=100)
    due_date: Optional[datetime.datetime] = None

class ToDo(ToDoCreate):
    ToDo_id: int
    reg_date: datetime.datetime

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    username: str = Field(max_length=12)

class User(UserCreate):
    user_id: int

    class Config:
        orm_mode = True

class ToDo_id(BaseModel):
    ToDo_id: int

class update(BaseModel):
    ToDo_id: int
    description: str = Field(max_length=100)