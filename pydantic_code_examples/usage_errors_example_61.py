
from typing_extensions import Self

from pydantic import BaseModel, PydanticUserError, validate_call

try:

    class A(BaseModel):
        @validate_call
        def func(self, arg: Self):
            pass

except PydanticUserError as exc_info:
    assert exc_info.code == 'invalid-self-type'
