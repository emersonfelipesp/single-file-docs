
from typing import Optional

from pydantic import BaseModel, PydanticUserError


class Foo(BaseModel):
    a: Optional['Bar'] = None


try:
    # this doesn't work, see raised error
    foo = Foo(a={'b': {'a': None}})
except PydanticUserError as exc_info:
    assert exc_info.code == 'class-not-fully-defined'


class Bar(BaseModel):
    b: 'Foo'


# this works, though
foo = Foo(a={'b': {'a': None}})
