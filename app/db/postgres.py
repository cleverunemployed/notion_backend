import sqlalchemy
from databases import Database

DATABASE_URL = "postgresql://user:password@localhost/my_postgres_database"

database = Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# Подключение базы данных при старте приложения
async def connect_to_db():
    await database.connect()

# Отключение базы данных при завершении работы приложения
async def disconnect_from_db():
    await database.disconnect()
