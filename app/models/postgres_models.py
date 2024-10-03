import sqlalchemy
from pydantic import BaseModel
from .postgres import metadata

items = sqlalchemy.Table(
    "items",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("description", sqlalchemy.String)
)

class PostgresItem(BaseModel):
    id: int
    name: str
    description: str
