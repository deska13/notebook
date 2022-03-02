from .base import Base
from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relation


class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(Text, nullable=False)
    
    notes = relation("Note", back_populates='category', cascade="all, delete")