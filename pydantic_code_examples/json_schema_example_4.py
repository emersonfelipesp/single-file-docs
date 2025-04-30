
from decimal import Decimal

from pydantic import BaseModel


class Model(BaseModel):
    a: Decimal = Decimal('12.34')


print(Model.model_json_schema(mode='validation'))
"""
{
    'properties': {
        'a': {
            'anyOf': [{'type': 'number'}, {'type': 'string'}],
            'default': '12.34',
            'title': 'A',
        }
    },
    'title': 'Model',
    'type': 'object',
}
"""

print(Model.model_json_schema(mode='serialization'))
"""
{
    'properties': {'a': {'default': '12.34', 'title': 'A', 'type': 'string'}},
    'title': 'Model',
    'type': 'object',
}
"""
