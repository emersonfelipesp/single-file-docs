
import json
from uuid import UUID

from pydantic import BaseModel, ValidationError


class MyModel(BaseModel):
    guid: UUID


data = {'guid': '12345678-1234-1234-1234-123456789012'}

print(MyModel.model_validate(data))  # OK: lax
#> guid=UUID('12345678-1234-1234-1234-123456789012')

print(
    MyModel.model_validate_json(json.dumps(data), strict=True)
)  # OK: strict, but from json
#> guid=UUID('12345678-1234-1234-1234-123456789012')

try:
    MyModel.model_validate(data, strict=True)  # Not OK: strict, from python
except ValidationError as exc:
    print(exc.errors(include_url=False))
    """
    [
        {
            'type': 'is_instance_of',
            'loc': ('guid',),
            'msg': 'Input should be an instance of UUID',
            'input': '12345678-1234-1234-1234-123456789012',
            'ctx': {'class': 'UUID'},
        }
    ]
    """
