
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: int


try:
    Model(x=2.2250738585072011e308)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'finite_number'
