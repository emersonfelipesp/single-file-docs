
from enum import Enum

from pydantic import BaseModel, Field, ValidationError


class MyEnum(str, Enum):
    foo = 'foo'


class Model(BaseModel):
    x: str = Field(strict=True)


try:
    Model(x=MyEnum.foo)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'string_sub_type'
