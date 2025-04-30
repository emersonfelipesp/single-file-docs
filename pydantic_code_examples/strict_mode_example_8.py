
from typing import Annotated

from typing_extensions import TypedDict

from pydantic import Field, TypeAdapter, ValidationError


class MyDict(TypedDict):
    x: Annotated[int, Field(strict=True)]


try:
    TypeAdapter(MyDict).validate_python({'x': '1'})
except ValidationError as exc:
    print(exc)
    """
    1 validation error for MyDict
    x
      Input should be a valid integer [type=int_type, input_value='1', input_type=str]
    """
