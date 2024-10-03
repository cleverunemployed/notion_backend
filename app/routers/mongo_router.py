from fastapi import APIRouter, Depends
from app.models.mongodb_models import MongoItem
from app.db.mongodb import get_mongo_client

router = APIRouter()

@router.get("/mongo_items")
async def get_mongo_items(db=Depends(get_mongo_client)):
    items = await db["items"].find().to_list(100)
    return items

@router.post("/mongo_items")
async def create_mongo_item(item: MongoItem, db=Depends(get_mongo_client)):
    new_item = await db["items"].insert_one(item.dict())
    return {"id": str(new_item.inserted_id)}
