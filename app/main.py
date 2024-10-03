from fastapi import FastAPI
from app.db.postgres import connect_to_db, disconnect_from_db
from app.routers import mongo_router, postgres_router

app = FastAPI()

# Подключаемся к PostgreSQL при старте приложения
@app.on_event("startup")
async def startup():
    await connect_to_db()

# Отключаем PostgreSQL при завершении работы приложения
@app.on_event("shutdown")
async def shutdown():
    await disconnect_from_db()

# Роуты для MongoDB и PostgreSQL
app.include_router(mongo_router.router, prefix="/mongo")
app.include_router(postgres_router.router, prefix="/postgres")
