
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    num: complex


try:
    Model(num=False)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'complex_type'
