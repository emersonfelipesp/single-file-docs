
from typing import Any, Callable

from pydantic import BaseModel, ImportString, ValidationError


class Model(BaseModel):
    x: ImportString[Callable[[Any], Any]]


Model(x='math:cos')  # OK

try:
    Model(x='os.path')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'callable_type'
