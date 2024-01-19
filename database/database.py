import datetime
import motor.motor_asyncio

class Database:

    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.clinton = self._client[database_name]
        self.col = self.clinton.USERS

BASE = declarative_base()


class CustomCaption(BASE):
    __tablename__ = "caption"
    id = Column(Integer, primary_key=True)
    caption = Column(String)
    
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
