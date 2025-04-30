
from pydantic import PydanticUserError, validate_call

# error
try:

    class A:
        @validate_call
        @classmethod
        def f1(cls): ...

except PydanticUserError as exc_info:
    assert exc_info.code == 'validate-call-type'


# correct
@classmethod
@validate_call
def f2(cls): ...
