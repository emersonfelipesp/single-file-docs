
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: bool


Model(x='true')  # OK

try:
    Model(x='test')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'bool_parsing'
