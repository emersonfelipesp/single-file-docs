
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    num: complex


try:
    # Complex numbers in json are expected to be valid complex strings.
    # This value `abc` is not a valid complex string.
    Model.model_validate_json('{"num": "abc"}')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'complex_str_parsing'
