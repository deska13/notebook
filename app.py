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
def delete_category(category_id):
    return db_query.delete_category_by_id(category_id)