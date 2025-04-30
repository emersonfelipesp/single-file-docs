
from typing_extensions import TypedDict

from pydantic import ConfigDict, TypeAdapter, ValidationError


class Inner(TypedDict):
    y: int


Inner.__pydantic_config__ = ConfigDict(strict=True)


class Outer(TypedDict):
    x: int
    inner: Inner


adapter = TypeAdapter(Outer)
print(adapter.validate_python({'x': '1', 'inner': {'y': 2}}))
#> {'x': 1, 'inner': {'y': 2}}


try:
    adapter.validate_python({'x': '1', 'inner': {'y': '2'}})
except ValidationError as exc:
    print(exc)
    """
    1 validation error for Outer
    inner.y
      Input should be a valid integer [type=int_type, input_value='2', input_type=str]
    """
