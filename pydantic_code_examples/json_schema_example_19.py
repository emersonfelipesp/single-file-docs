
import json

from pydantic import BaseModel, ConfigDict


def make_title(model: type) -> str:
    return f'Title-{model.__name__}'


class Person(BaseModel):
    model_config = ConfigDict(model_title_generator=make_title)
    name: str
    age: int


print(json.dumps(Person.model_json_schema(), indent=2))
"""
{
  "properties": {
    "name": {
      "title": "Name",
      "type": "string"
    },
    "age": {
      "title": "Age",
      "type": "integer"
    }
  },
  "required": [
    "name",
    "age"
  ],
  "title": "Title-Person",
  "type": "object"
}
"""
