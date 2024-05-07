from sqlalchemy.orm import Session

from . import models, schemas


def create_task(db: Session, task: schemas.Task):
    if task.operator == '+':
        result_value = task.x + task.y
    elif task.operator == '-':
        result_value = task.x - task.y
    elif task.operator == '*':
        result_value = task.x * task.y
    elif task.operator == '/':
        result_value = task.x / task.y
    else:
        raise ValueError(f'Недопустимый оператор: {task.operator}')

    db_task = models.Task(
        x=task.x,
        y=task.y,
        operator=task.operator,
        result=result_value
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task
