from sqlalchemy import Boolean, Column, Integer, String
from database import base

class User(base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    