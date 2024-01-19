import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import Config
import asyncpgsa

BASE = declarative_base()


class CustomCaption(BASE):
    __tablename__ = "caption"
    id = Column(Integer, primary_key=True)
    caption = Column(String)


DB_URL = Config.DB_URL
engine = create_engine(DB_URL)
asyncpgsa.sa.init(engine)

async def create_table():
    async with engine.acquire() as conn:
        await conn.execute('''CREATE TABLE IF NOT EXISTS caption (
                                id serial PRIMARY KEY,
                                caption varchar(255) NOT NULL)''')


async def update_caption(id, caption):
    async with engine.acquire() as conn:
        await conn.execute(
            CustomCaption.__table__.insert().values(id=id, caption=caption)
        )


async def del_caption(id):
    async with engine.acquire() as conn:
        await conn.execute(
            CustomCaption.__table__.delete().where(CustomCaption.id == id)
        )


async def get_caption(id):
    async with engine.acquire() as conn:
        result = await conn.execute(
            CustomCaption.__table__.select().where(CustomCaption.id == id)
        )
        return await result.first()
