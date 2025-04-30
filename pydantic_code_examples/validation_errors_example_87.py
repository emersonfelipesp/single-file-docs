
from pydantic import BaseModel, Field, ValidationError


class Model(BaseModel):
    x: list[int] = Field(min_length=3)


try:
    Model(x=[1, 2])
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'too_short'
