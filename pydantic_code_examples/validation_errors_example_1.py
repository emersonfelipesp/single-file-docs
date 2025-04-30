
from typing import NamedTuple

from pydantic import BaseModel, ValidationError


class MyNamedTuple(NamedTuple):
    x: int


class MyModel(BaseModel):
    field: MyNamedTuple


try:
    MyModel.model_validate({'field': 'invalid'})
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'arguments_type'
