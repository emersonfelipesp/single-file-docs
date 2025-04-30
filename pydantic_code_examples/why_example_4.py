
    from datetime import datetime

    from pydantic import BaseModel


    class Address(BaseModel):
        street: str
        city: str
        zipcode: str


    class Meeting(BaseModel):
        when: datetime
        where: Address
        why: str = 'No idea'


    print(Meeting.model_json_schema())
    """
    {
        '$defs': {
            'Address': {
                'properties': {
                    'street': {'title': 'Street', 'type': 'string'},
                    'city': {'title': 'City', 'type': 'string'},
                    'zipcode': {'title': 'Zipcode', 'type': 'string'},
                },
                'required': ['street', 'city', 'zipcode'],
                'title': 'Address',
                'type': 'object',
            }
        },
        'properties': {
            'when': {'format': 'date-time', 'title': 'When', 'type': 'string'},
            'where': {'$ref': '#/$defs/Address'},
            'why': {'default': 'No idea', 'title': 'Why', 'type': 'string'},
        },
        'required': ['when', 'where'],
        'title': 'Meeting',
        'type': 'object',
    }
    """
    