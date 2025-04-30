
from pydantic import BaseModel, Field, HttpUrl, ValidationError


class Model(BaseModel):
    x: HttpUrl = Field(strict=True)


try:
    Model(x='http:////example.com')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'url_syntax_violation'
