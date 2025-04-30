
from pydantic import BaseModel, ConfigDict, ValidationError


class MyBaseModel(BaseModel):
    model_config = ConfigDict(strict=True)


class Inner(MyBaseModel):
    y: int


class Outer(MyBaseModel):
    x: int
    inner: Inner


try:
    Outer.model_validate({'x': 1, 'inner': {'y': '2'}})
except ValidationError as exc:
    print(exc)
    """
    1 validation error for Outer
    inner.y
      Input should be a valid integer [type=int_type, input_value='2', input_type=str]
    """
