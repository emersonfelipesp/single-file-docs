 {hl_lines="1 11-12"}
from typing import Any

from pydantic import BaseModel


class Knight(BaseModel):
    title: str
    age: int
    color: str = 'blue'


age_str: Any = '23'
lancelot = Knight(title='Sir Lancelot', age=age_str)
