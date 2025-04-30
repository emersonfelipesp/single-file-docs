
import dataclasses
from typing import Optional

from pydantic import Field, TypeAdapter
from pydantic.dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str = 'John Doe'
    friends: list[int] = dataclasses.field(default_factory=lambda: [0])
    age: Optional[int] = dataclasses.field(
        default=None,
        metadata={'title': 'The age of the user', 'description': 'do not lie!'},
    )
    height: Optional[int] = Field(None, title='The height in cm', ge=50, le=300)


user = User(id='42')
print(TypeAdapter(User).json_schema())
"""
{
    'properties': {
        'id': {'title': 'Id', 'type': 'integer'},
        'name': {'default': 'John Doe', 'title': 'Name', 'type': 'string'},
        'friends': {
            'items': {'type': 'integer'},
            'title': 'Friends',
            'type': 'array',
        },
        'age': {
            'anyOf': [{'type': 'integer'}, {'type': 'null'}],
            'default': None,
            'description': 'do not lie!',
            'title': 'The age of the user',
        },
        'height': {
            'anyOf': [
                {'maximum': 300, 'minimum': 50, 'type': 'integer'},
                {'type': 'null'},
            ],
            'default': None,
            'title': 'The height in cm',
        },
    },
    'required': ['id'],
    'title': 'User',
    'type': 'object',
}
"""
