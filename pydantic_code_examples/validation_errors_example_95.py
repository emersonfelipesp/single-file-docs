
from pydantic import BaseModel, HttpUrl, ValidationError


class Model(BaseModel):
    x: HttpUrl


try:
    Model(x='ftp://example.com')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'url_scheme'
