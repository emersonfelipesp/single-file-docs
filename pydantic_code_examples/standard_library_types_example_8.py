
from typing import Optional

from pydantic import BaseModel


class Model(BaseModel):
    simple_list: Optional[list] = None
    list_of_ints: Optional[list[int]] = None


print(Model(simple_list=['1', '2', '3']).simple_list)
#> ['1', '2', '3']
print(Model(list_of_ints=['1', '2', '3']).list_of_ints)
#> [1, 2, 3]
