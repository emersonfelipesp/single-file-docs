
from datetime import date, datetime

from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: date


Model(x='2023-01-01')  # OK
Model(x=datetime(2023, 1, 1))  # OK

try:
    Model(x=datetime(2023, 1, 1, 12))
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'date_from_datetime_inexact'
