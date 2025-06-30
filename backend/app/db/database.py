from databases import Database
from sqlalchemy.ext.declarative import declarative_base

database = Database("postgresql+asyncpg://kullanici:parola@localhost:5432/saasdb")
Base = declarative_base()

async def connect_to_db():
    if not database.is_connected:
        await database.connect()

async def disconnect_from_db():
    if database.is_connected:
        await database.disconnect()

