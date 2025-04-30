
from pydantic import PydanticUserError, validate_call

# error
try:

    class A1:
        def __call__(self): ...

    validate_call(A1())

except PydanticUserError as exc_info:
    assert exc_info.code == 'validate-call-type'


# correct
class A2:
    @validate_call
    def __call__(self): ...
