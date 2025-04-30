
from pydantic import PydanticUserError, validate_call

try:

    class A:
        def f(): ...

    validate_call(A().f)
except PydanticUserError as exc_info:
    assert exc_info.code == 'validate-call-type'
