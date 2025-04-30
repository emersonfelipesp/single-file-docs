
from pydantic import BaseModel, Field, ValidationError


class Model(BaseModel):
    x: int = Field(ge=10)


try:
    Model(x=9)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'greater_than_equal'
