from sqlalchemy import Column, Integer, Text, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Note(Base):
    __tablename__ = "note"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    body = Column(Text, nullable=False)
    pinned = Column(Boolean, default=False, nullable=False)
