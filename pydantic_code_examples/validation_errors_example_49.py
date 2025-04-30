
from pydantic import BaseModel, ValidationError


class Nested:
    x: str


class Model(BaseModel):
    y: type[Nested]


try:
    Model(y='test')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'is_subclass_of'
