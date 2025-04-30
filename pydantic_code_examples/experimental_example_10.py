
from typing import Annotated

from annotated_types import MinLen
from typing_extensions import TypedDict

from pydantic import TypeAdapter


class Foobar(TypedDict, total=False):
    a: int
    b: Annotated[str, MinLen(5)]


ta = TypeAdapter(Foobar)

v = ta.validate_json(
    '{"a": 1, "b": "12', experimental_allow_partial=True  # (1)!
)
print(v)
#> {'a': 1}

v = ta.validate_json(
    '{"a": 1, "b": "12"}', experimental_allow_partial=True  # (2)!
)
print(v)
#> {'a': 1}
