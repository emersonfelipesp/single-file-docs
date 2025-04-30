
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    a: int
    b: int


# simply validating a dict
m = Model.model_validate({'a': 1, 'b': 2})
print(m)
#> a=1 b=2

# validating an existing model instance
print(Model.model_validate(m))
#> a=1 b=2

try:
    Model.model_validate('not an object')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'model_type'
