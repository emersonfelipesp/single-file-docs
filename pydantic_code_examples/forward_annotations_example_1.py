
from __future__ import annotations

from pydantic import BaseModel

MyInt = int


class Model(BaseModel):
    a: MyInt
    # Without the future import, equivalent to:
    # a: 'MyInt'


print(Model(a='1'))
#> a=1
