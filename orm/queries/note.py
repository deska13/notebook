import traceback
from ..models import *
from .engine import session


def add_note(category_id, title, content):
    try:
        session.query(Category).filter(Category.id == category_id).one()
    except:
        return ("Неверный id категории")
    
    note = Note(
        category_id=category_id,
        title=title,
        content=content
    )
    session.add(note)
    session.commit()
    return note.id


def get_note_by_id(note_id):
    try:
        rows = session.query(
            Note,
            Category
        ).filter(
            Note.id == note_id,
            Note.category_id == Category.id
            ).all()
        for row in rows:
            note, category = row
            print(vars(note))
            print(vars(category))
    except:
        traceback.print_exc()
        return ("Неверный id категории")



def delete_note():
    return