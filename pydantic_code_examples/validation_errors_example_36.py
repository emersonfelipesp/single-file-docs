
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: float


try:
    Model(x=None)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'float_type'
