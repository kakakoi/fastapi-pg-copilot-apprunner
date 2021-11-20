from typing import List

import databases

import sqlalchemy

from fastapi import FastAPI
from pydantic import BaseModel

import os
import json
import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


secret_name = 'DB_SECRET'
secret_text = json.loads(os.environ[secret_name])

DATABASE = 'postgresql'
USER = secret_text['username']
PASSWORD = secret_text['password']
# HOST = 'localhost'
HOST = secret_text['host']
PORT = secret_text['port']
DB_NAME = secret_text['dbname']

# SQLAlchemy specific code, as with any other app
TEST_DATABASE_URL = "sqlite:///./test.db"
DATABASE_URL = '{}://{}:{}@{}:{}/{}'.format(DATABASE, USER, PASSWORD, HOST, PORT, DB_NAME)

TESTING = os.environ.get('TESTING')

if TESTING:
    DATABASE_URL = TEST_DATABASE_URL

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

notes = sqlalchemy.Table(
    "notes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String, server_default="blank"),
    sqlalchemy.Column("text", sqlalchemy.String),
    sqlalchemy.Column("completed", sqlalchemy.Boolean),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL
)
if TESTING:
    metadata.drop_all(engine)
metadata.create_all(engine)

class NoteIn(BaseModel):
    title: str
    text: str
    completed: bool


class Note(BaseModel):
    id: int
    title: str
    text: str
    completed: bool


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/notes/", response_model=List[Note])
async def read_notes():
    query = notes.select()
    return await database.fetch_all(query)


@app.post("/notes/", response_model=Note)
async def create_note(note: NoteIn):
    query = notes.insert().values(text=note.text, title=note.title, completed=note.completed)
    last_record_id = await database.execute(query)
    return {**note.dict(), "id": last_record_id}
