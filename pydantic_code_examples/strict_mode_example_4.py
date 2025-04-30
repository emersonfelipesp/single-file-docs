
from dataclasses import dataclass

from pydantic import TypeAdapter, ValidationError


@dataclass
class MyDataclass:
    x: int


try:
    TypeAdapter(MyDataclass).validate_python({'x': '123'}, strict=True)
except ValidationError as exc:
    print(exc)
    """
    1 validation error for MyDataclass
      Input should be an instance of MyDataclass [type=dataclass_exact_type, input_value={'x': '123'}, input_type=dict]
    """
