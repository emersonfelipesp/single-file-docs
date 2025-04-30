
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: set[object]


class Unhashable:
    __hash__ = None


try:
    Model(x=[{'a': 'b'}, Unhashable()])
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'set_item_not_hashable'
    print(repr(exc.errors()[1]['type']))
    #> 'set_item_not_hashable'
