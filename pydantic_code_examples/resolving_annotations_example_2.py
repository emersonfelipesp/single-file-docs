 {requires="3.12" lint="skip"}
from __future__ import annotations

from pydantic import BaseModel


class Foo(BaseModel):
    f: MyType
    # Given the future import above, this is equivalent to:
    # f: 'MyType'


type MyType = int

print(Foo.__annotations__)
#> {'f': 'MyType'}
