
from typing_extensions import TypedDict, Unpack

from pydantic import PydanticUserError, validate_call


class TD(TypedDict):
    a: int


try:

    @validate_call
    def func(a: int, **kwargs: Unpack[TD]):
        pass

except PydanticUserError as exc_info:
    assert exc_info.code == 'overlapping-unpack-typed-dict'
