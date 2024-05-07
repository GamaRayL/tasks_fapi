from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from . import db, schemas, crud

db.create_database()

app = FastAPI()


@app.post('/tasks/', response_model=schemas.Task)
def create_task(
    task: schemas.Task,
    database: Session = Depends(db.get_db)
):
    return crud.create_task(database, task=task)


@app.get('/tasks/{task_id}', response_model=schemas.TaskResult)
def read_task(
    task_id: int,
    database: Session = Depends(db.get_db)
):
    db_task = crud.get_task(database, task_id=task_id)

    if db_task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Задача не найдена'
        )

    return schemas.TaskResult(result=db_task.result)


@app.get('/tasks/', response_model=list[schemas.Task])
def read_tasks(
    skip: int = 0,
    limit: int = 10,
    database: Session = Depends(db.get_db)
):
    tasks = crud.get_tasks(database, skip=skip, limit=limit)
    return tasks
