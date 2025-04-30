
from pydantic import BaseModel, HttpUrl, ValidationError


class Model(BaseModel):
    x: HttpUrl


try:
    Model(x='x' * 2084)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'url_too_long'
