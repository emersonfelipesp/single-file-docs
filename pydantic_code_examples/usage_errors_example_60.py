
from typing_extensions import Self

from pydantic import PydanticUserError, validate_call

try:

    @validate_call
    def func(self: Self):
        pass

except PydanticUserError as exc_info:
    assert exc_info.code == 'invalid-self-type'
