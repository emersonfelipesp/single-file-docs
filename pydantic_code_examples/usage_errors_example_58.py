
from typing_extensions import Unpack

from pydantic import PydanticUserError, validate_call

try:

    @validate_call
    def func(**kwargs: Unpack[int]):
        pass

except PydanticUserError as exc_info:
    assert exc_info.code == 'unpack-typed-dict'
