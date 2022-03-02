from sqlmodel import Session
from ..models import *
from .engine import session


def add_category(category_name):
    # создаём строку
    category = Category(
        name=category_name
    )
    # добавляем запись
    session.add(category)
    # фиксируем запись
    session.commit()


def get_categories():
    categories = session.query(Category).all()
    # "SELECT * FROM category"
    return categories


def delete_category_by_id(id):
    category = session.query(Category).filter(Category.id == id).one()
    session.delete(category)
    session.commit()