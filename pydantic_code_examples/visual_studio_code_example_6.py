 {hl_lines="1 11"}
from typing import Any, cast

from pydantic import BaseModel


class Knight(BaseModel):
    title: str
    age: int
    color: str = 'blue'


lancelot = Knight(title='Sir Lancelot', age=cast(Any, '23'))
