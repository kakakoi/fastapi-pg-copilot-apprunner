from fastapi import APIRouter, Depends
from typing import Optional, List

from backend.schemas import note as schema
from backend.models.note import notes as model

from backend.db import get_db
from databases.core import Database as DB

router = APIRouter()

@router.get("/notes/", response_model=List[schema.Note])
async def read_notes(offset: int = 0, limit = 100, db: DB = Depends(get_db)):
    query = model.select().offset(offset).limit(limit)
    return await db.fetch_all(query)

@router.post("/notes/", response_model=schema.Note)
async def create_note(note: schema.NoteIn, db: DB = Depends(get_db)):
    query = model.insert().values(text=note.text, title=note.title, completed=note.completed)
    last_record_id = await db.execute(query)
    return {**note.dict(), "id": last_record_id}
