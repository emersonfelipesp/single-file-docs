 {output="json"}
import json
from typing import Annotated
from uuid import uuid4

from pydantic import BaseModel, Field


class Foo(BaseModel):
    id: Annotated[str, Field(default_factory=lambda: uuid4().hex)]
    name: Annotated[str, Field(max_length=256)] = Field(
        'Bar', title='CustomName'
    )


print(json.dumps(Foo.model_json_schema(), indent=2))
"""
{
  "properties": {
    "id": {
      "title": "Id",
      "type": "string"
    },
    "name": {
      "default": "Bar",
      "maxLength": 256,
      "title": "CustomName",
      "type": "string"
    }
  },
  "title": "Foo",
  "type": "object"
}
"""
