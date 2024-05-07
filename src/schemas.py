from datetime import datetime

from pydantic import BaseModel, field_validator


class Task(BaseModel):
    id: int
    x: int
    y: int
    operator: str
    result: int | float | None
    created_on: datetime
    updated_on: datetime

    @field_validator('operator')
    def validate_operator(cls, value: str) -> str:
        operators = ['+', '-', '*', '/']
        if value not in operators:
            raise ValueError(
                f'Ваш оператор ({value}) не соответствует: {operators}'
            )
        return value
