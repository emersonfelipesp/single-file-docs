
from pydantic import BaseModel, Json, ValidationError


class Model(BaseModel):
    x: Json


try:
    Model(x='test')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'json_invalid'
