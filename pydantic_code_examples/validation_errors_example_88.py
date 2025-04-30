
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: tuple[int]


try:
    Model(x=None)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'tuple_type'
