
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: str


try:
    Model(x=b'\x81')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'string_unicode'
