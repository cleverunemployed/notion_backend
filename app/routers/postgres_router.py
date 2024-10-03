from fastapi import APIRouter
from app.db.postgres import database
from app.models.postgres_models import PostgresItem, items

router = APIRouter()

@router.get("/postgres_items")
async def get_postgres_items():
    query = items.select()
    return await database.fetch_all(query)

@router.post("/postgres_items")
async def create_postgres_item(item: PostgresItem):
    query = items.insert().values(name=item.name, description=item.description)
    last_record_id = await database.execute(query)
    return {"id": last_record_id}
