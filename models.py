from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    chat_id = Column(Integer, primary_key=True)
    username = Column(String, nullable=True)
