
from pydantic import BaseModel, Field, ValidationError


class Model(BaseModel):
    x: bytes = Field(min_length=3)


try:
    Model(x=b't')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'bytes_too_short'
