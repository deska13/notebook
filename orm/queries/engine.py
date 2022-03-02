from sqlalchemy.orm import Session
from sqlalchemy import create_engine

db_file = "C:/Users/deska/OneDrive/Рабочий стол/teach/learn_orm/notebook/db/blog.sqlite"

conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'
engine = create_engine(conn_str, echo=False)
session = Session(engine)