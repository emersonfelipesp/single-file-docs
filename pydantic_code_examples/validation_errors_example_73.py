
from typing import Set

from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: Set[int]


try:
    Model(x='test')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'set_type'
