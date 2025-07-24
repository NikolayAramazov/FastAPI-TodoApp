from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class ToDo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, default="")
    completed = Column(Boolean, default=False)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)