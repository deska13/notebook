from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# подключаем таблицы
from orm.models.base import Base
from orm.models import *

import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db_file = BASE_DIR + "/db/blog.sqlite"

conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'
print("Подключение к БД")
engine = create_engine(conn_str, echo=False)
session_factory = Session(bind=engine)

Base.metadata.create_all(engine)