
from datetime import timedelta

from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: timedelta


try:
    Model(x=None)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'time_delta_type'
