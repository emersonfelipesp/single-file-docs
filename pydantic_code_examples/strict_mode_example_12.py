
from pydantic import BaseModel, ConfigDict, ValidationError


class Inner(BaseModel):
    y: int


class Outer(BaseModel):
    model_config = ConfigDict(strict=True)

    x: int
    inner: Inner


print(Outer(x=1, inner=Inner(y='2')))
#> x=1 inner=Inner(y=2)

try:
    Outer(x='1', inner=Inner(y='2'))
except ValidationError as exc:
    print(exc)
    """
    1 validation error for Outer
    x
      Input should be a valid integer [type=int_type, input_value='1', input_type=str]
    """
