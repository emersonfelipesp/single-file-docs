
import json
from uuid import UUID

from pydantic import BaseModel, TypeAdapter, ValidationError

try:
    TypeAdapter(list[int]).validate_json('["1", 2, "3"]', strict=True)
except ValidationError as exc:
    print(exc)
    """
    2 validation errors for list[int]
    0
      Input should be a valid integer [type=int_type, input_value='1', input_type=str]
    2
      Input should be a valid integer [type=int_type, input_value='3', input_type=str]
    """


class Model(BaseModel):
    x: int
    y: UUID


data = {'x': '1', 'y': '12345678-1234-1234-1234-123456789012'}
try:
    Model.model_validate(data, strict=True)
except ValidationError as exc:
    # Neither x nor y are valid in strict mode from python:
    print(exc)
    """
    2 validation errors for Model
    x
      Input should be a valid integer [type=int_type, input_value='1', input_type=str]
    y
      Input should be an instance of UUID [type=is_instance_of, input_value='12345678-1234-1234-1234-123456789012', input_type=str]
    """

json_data = json.dumps(data)
try:
    Model.model_validate_json(json_data, strict=True)
except ValidationError as exc:
    # From JSON, x is still not valid in strict mode, but y is:
    print(exc)
    """
    1 validation error for Model
    x
      Input should be a valid integer [type=int_type, input_value='1', input_type=str]
    """
