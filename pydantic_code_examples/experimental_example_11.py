
from typing import Annotated

from annotated_types import Ge

from pydantic import TypeAdapter

ta = TypeAdapter(list[Annotated[int, Ge(10)]])
v = ta.validate_python([20, 30, 4], experimental_allow_partial=True)  # (1)!
print(v)
#> [20, 30]

ta = TypeAdapter(list[int])

v = ta.validate_python([1, 2, 'wrong'], experimental_allow_partial=True)  # (2)!
print(v)
#> [1, 2]
