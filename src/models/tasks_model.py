from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    Numeric,
    String, DateTime
)

from src.db import Base


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    x = Column(Integer)
    y = Column(Integer)
    operator = Column(String(1))
    result = Column(Numeric, nullable=False)

    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
