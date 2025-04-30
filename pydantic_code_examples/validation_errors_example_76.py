
from pydantic import BaseModel, Field, ValidationError


class Model(BaseModel):
    x: str = Field(max_length=3)


try:
    Model(x='test')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'string_too_long'
