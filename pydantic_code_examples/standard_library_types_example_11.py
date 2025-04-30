
from typing import Deque, Optional

from pydantic import BaseModel


class Model(BaseModel):
    deque: Optional[Deque[int]] = None


print(Model(deque=[1, 2, 3]).deque)
#> deque([1, 2, 3])
