
from pydantic import BaseModel, Field


class Knight(BaseModel):
    title: str = Field(default='Sir Lancelot')  # this is okay
    age: int = Field(
        23
    )  # this works fine at runtime but will case an error for pyright


lance = Knight()  # error: Argument missing for parameter "age"
