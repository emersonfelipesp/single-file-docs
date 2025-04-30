
from pydantic import AnyUrl, BaseModel, ValidationError


class Model(BaseModel):
    x: AnyUrl


try:
    Model(x='test')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'url_parsing'
