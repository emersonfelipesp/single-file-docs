
from typing import Optional, Set

from pydantic import BaseModel


class Model(BaseModel):
    simple_set: Optional[set] = None
    set_of_ints: Optional[Set[int]] = None


print(Model(simple_set={'1', '2', '3'}).simple_set)
#> {'1', '2', '3'}
print(Model(simple_set=['1', '2', '3']).simple_set)
#> {'1', '2', '3'}
print(Model(set_of_ints=['1', '2', '3']).set_of_ints)
#> {1, 2, 3}
