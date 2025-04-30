
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: None


try:
    Model(x=1)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'none_required'
