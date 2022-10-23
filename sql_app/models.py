####Datebase用
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.sql.functions import user
from sqlalchemy.sql.sqltypes import Date
from database import Base

class ToDo(Base):
    __tablename__ = "ToDo"

    user_id = Column(Integer, ForeignKey('users.user_id', ondelete='SET NULL'), nullable=False)
    ToDo_id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    reg_date = Column(DateTime, nullable=False)
    due_date = Column(DateTime, nullable=True)

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)