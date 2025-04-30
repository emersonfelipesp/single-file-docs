
from typing import Iterable

from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    y: Iterable


try:
    Model(y=123)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'iterable_type'
