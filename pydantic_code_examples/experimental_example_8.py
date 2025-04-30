 {title="Errors in last element ignored"}
from typing import Annotated

from annotated_types import MinLen

from pydantic import BaseModel, TypeAdapter


class MyModel(BaseModel):
    a: int
    b: Annotated[str, MinLen(5)]


ta = TypeAdapter(list[MyModel])
v = ta.validate_json(
    '[{"a": 1, "b": "12345"}, {"a": 1,',
    experimental_allow_partial=True,
)
print(v)
#> [MyModel(a=1, b='12345')]
