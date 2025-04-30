
from pydantic import ValidationError, validate_call


@validate_call
def foo(*, a: int):
    return a


try:
    foo(2)
except ValidationError as exc:
    print(repr(exc.errors()[1]['type']))
    #> 'unexpected_positional_argument'
