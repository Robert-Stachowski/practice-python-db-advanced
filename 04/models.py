from sqlalchemy import Integer, String, Column, Float, DateTime
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class Measurement(Base):
    __tablename__ = "measurement"

    id = Column(Integer, primary_key=True)
    device_name = Column(String, nullable=False)
    value = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=False)