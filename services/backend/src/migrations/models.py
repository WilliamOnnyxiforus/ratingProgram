from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Integer, String, func

Base = declarative_base()
metadata = Base.metadata

william = "Testing variable import"

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True)
    rate = Column(Integer)
    comment = Column(String(200))
    date_new = Column(DateTime, default=func.now())