
from pydantic import BaseModel, Field, ValidationError


class Model(BaseModel):
    x: str = Field('test', frozen=True)


model = Model()

try:
    model.x = 'test1'
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'frozen_field'

try:
    del model.x
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'frozen_field'
