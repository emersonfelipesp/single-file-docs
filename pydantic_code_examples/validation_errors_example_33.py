
from pydantic import BaseModel, ConfigDict, ValidationError


class Model(BaseModel):
    x: str

    model_config = ConfigDict(extra='forbid')


try:
    Model(x='test', y='test')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'extra_forbidden'
