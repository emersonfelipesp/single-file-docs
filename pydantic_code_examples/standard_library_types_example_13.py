
from typing import FrozenSet, Optional

from pydantic import BaseModel


class Model(BaseModel):
    simple_frozenset: Optional[frozenset] = None
    frozenset_of_ints: Optional[FrozenSet[int]] = None


m1 = Model(simple_frozenset=['1', '2', '3'])
print(type(m1.simple_frozenset))
#> <class 'frozenset'>
print(sorted(m1.simple_frozenset))
#> ['1', '2', '3']

m2 = Model(frozenset_of_ints=['1', '2', '3'])
print(type(m2.frozenset_of_ints))
#> <class 'frozenset'>
print(sorted(m2.frozenset_of_ints))
#> [1, 2, 3]
