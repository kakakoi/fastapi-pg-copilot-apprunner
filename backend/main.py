from typing import List

from fastapi import FastAPI

from backend.db import metadata, database, engine, TESTING
from backend.routers import note, root

app = FastAPI()
app.include_router(note.router, tags=['note'])
app.include_router(root.router)

if TESTING:
    metadata.drop_all(engine)
metadata.create_all(engine)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()