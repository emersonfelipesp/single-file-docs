
from pydantic import BaseModel, Field, ValidationError


class Model(BaseModel):
    x: str = Field(min_length=3)


try:
    Model(x='t')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'string_too_short'
