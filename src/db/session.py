import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = 'postgresql://postgres@localhost/tasks_db'
engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        logging.info('Создание соединения с БД')
        yield db
    finally:
        logging.info("Соединение с БД закрыто")
        db.close()
