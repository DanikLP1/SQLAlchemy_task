from sqlalchemy.orm import Session
from models import Note, User
from schemas import NoteBase, NoteCreate, UserCreate

def get_notes(db: Session):
    return db.query(Note).all()

def get_note(db: Session, note_id: int):
    return db.query(Note).filter(Note.id == note_id).first()

def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_notes_by_user(db: Session, user_id: int):
    return db.query(Note).filter(Note.user_id == user_id).all()

def create_note(db: Session, note: NoteCreate):
    db_note = Note(**note.model_dump())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def update_note(db: Session, note_id: int, data: NoteBase):
    db_note = db.query(Note).filter(Note.id == note_id).first()
    if db_note:
        db_note.title = data.title
        db_note.content = data.content
        db.commit()
        db.refresh(db_note)
    return db_note

def delete_note(db: Session, note_id: int):
    db_note = db.query(Note).filter(Note.id == note_id).first()
    if db_note:
        db.delete(db_note)
        db.commit()
    return db_note
