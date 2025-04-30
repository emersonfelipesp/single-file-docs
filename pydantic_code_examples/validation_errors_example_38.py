
from pydantic import BaseModel, ConfigDict, ValidationError


class Model(BaseModel):
    x: int

    model_config = ConfigDict(frozen=True)


m = Model(x=1)

try:
    m.x = 2
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'frozen_instance'

try:
    del m.x
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'frozen_instance'
