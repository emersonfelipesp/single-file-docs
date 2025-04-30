
from datetime import datetime, timezone

from pydantic import BaseModel, NaiveDatetime, ValidationError


class Model(BaseModel):
    x: NaiveDatetime


try:
    Model(x=datetime.now(tz=timezone.utc))
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'timezone_naive'
