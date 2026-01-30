from sqlalchemy import Integer, String, create_engine, Column
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    priority = Column(Integer, nullable=False)