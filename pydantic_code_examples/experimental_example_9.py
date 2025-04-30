
from typing import Annotated

from annotated_types import MinLen

from pydantic import BaseModel, TypeAdapter, ValidationError


class MyModel(BaseModel):
    a: int = 1
    b: list[Annotated[str, MinLen(5)]] = []  # (1)!


ta = TypeAdapter(MyModel)
try:
    v = ta.validate_json(
        '{"a": 1, "b": ["12345", "12', experimental_allow_partial=True
    )
except ValidationError as e:
    print(e)
    """
    1 validation error for MyModel
    b.1
      String should have at least 5 characters [type=string_too_short, input_value='12', input_type=str]
    """
