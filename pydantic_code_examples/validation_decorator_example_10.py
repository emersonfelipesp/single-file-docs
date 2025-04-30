
from pydantic import validate_call


@validate_call
def validate_foo(a: int, b: int):
    def foo():
        return a + b

    return foo


foo = validate_foo(a=1, b=2)
print(foo())
#> 3
