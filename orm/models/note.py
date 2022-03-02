from datetime import datetime
from .base import Base
from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relation


class Note(Base):
    __tablename__ = 'notes'
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    time_create = Column(DateTime, default=datetime.now())
    title = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    
    category = relation('Category')