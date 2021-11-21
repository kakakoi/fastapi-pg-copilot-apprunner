import sqlalchemy
from backend.db import metadata

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String, server_default="blank"),
    sqlalchemy.Column("completed", sqlalchemy.Boolean),
)