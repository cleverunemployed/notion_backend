from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from fastapi import FastAPI

MONGO_DB_URL = "mongodb://localhost:27017"
DATABASE_NAME = "my_mongo_database"

client = AsyncIOMotorClient(MONGO_DB_URL)
mongodb = client[DATABASE_NAME]

async def get_mongo_client():
    return mongodb
