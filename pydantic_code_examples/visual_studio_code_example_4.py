 {hl_lines="10"}
from pydantic import BaseModel


class Knight(BaseModel):
    title: str
    age: int
    color: str = 'blue'


lancelot = Knight(title='Sir Lancelot', age='23')  # pyright: ignore
