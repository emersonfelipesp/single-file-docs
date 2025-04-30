
from pydantic import TypeAdapter, ValidationError
from pydantic.dataclasses import dataclass


@dataclass(config={'extra': 'forbid'})
class Foo:
    bar: int


try:
    TypeAdapter(Foo).validate_python({'bar': 1, 'foobar': 2})
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'unexpected_keyword_argument'
