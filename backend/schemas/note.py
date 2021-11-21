from pydantic import BaseModel

class NoteIn(BaseModel):
    title: str
    text: str
    completed: bool


class Note(BaseModel):
    id: int
    title: str
    text: str
    completed: bool