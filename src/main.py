from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import crud, db, schemas

db.create_database()

app = FastAPI()


@app.post('/tasks/', response_model=schemas.Task)
def create_task(task: schemas.Task, db: Session = Depends(db.get_db)):
    return crud.create_task(db=db, task=task)
