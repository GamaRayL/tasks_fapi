from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from crud import create_task
from db import get_db, create_database
from schemas import Task

create_database()

app = FastAPI()


@app.post('/tasks/', response_model=Task)
def create_task(task: Task, db: Session = Depends(get_db)):
    return create_task(db=db, task=task)
