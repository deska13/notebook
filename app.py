from fastapi import FastAPI
import orm.queries as db_query


app = FastAPI()


@app.post('/add_category/category_name={category_name}')
def add_category(category_name: str):
    return db_query.add_category(category_name)


@app.get('/get_categories')
def get_categories():
    return db_query.get_categories()


@app.delete('/delete_category/category_id={category_id}')
def delete_category(category_id: int):
    return db_query.delete_category_by_id(category_id)


@app.post('/add_note/category_id={category_id}&&title={title}&&content={content}')
def add_note(category_id: int, title: str, content: str):
    return db_query.add_note(category_id, title, content)


@app.get('/get_note/note_id={note_id}')
def get_note(note_id: int):
    return db_query.get_note_by_id(note_id)