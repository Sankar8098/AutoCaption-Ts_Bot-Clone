import motor.motor_asyncio
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

BASE = declarative_base()

class CustomCaption(BASE):
    __tablename__ = "caption"
    id = Column(Integer, primary_key=True)
    caption = Column(String)

class Database:

    def __init__(self, uri, database_name):
        # Assuming you are using SQLAlchemy for 'engine'
        self.engine = create_engine(uri)
        BASE.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    async def update_caption(self, id, caption):
        new_caption = CustomCaption(id=id, caption=caption)
        self.session.add(new_caption)
        self.session.commit()

    async def del_caption(self, id):
        caption_to_delete = self.session.query(CustomCaption).filter_by(id=id).first()
        if caption_to_delete:
            self.session.delete(caption_to_delete)
            self.session.commit()

    async def get_caption(self, id):
        return self.session.query(CustomCaption).filter_by(id=id).first()
