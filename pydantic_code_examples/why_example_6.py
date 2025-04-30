
    from datetime import datetime

    from typing_extensions import NotRequired, TypedDict

    from pydantic import TypeAdapter


    class Meeting(TypedDict):
        when: datetime
        where: bytes
        why: NotRequired[str]


    meeting_adapter = TypeAdapter(Meeting)
    m = meeting_adapter.validate_python(  # (1)!
        {'when': '2020-01-01T12:00', 'where': 'home'}
    )
    print(m)
    #> {'when': datetime.datetime(2020, 1, 1, 12, 0), 'where': b'home'}
    meeting_adapter.dump_python(m, exclude={'where'})  # (2)!

    print(meeting_adapter.json_schema())  # (3)!
    """
    {
        'properties': {
            'when': {'format': 'date-time', 'title': 'When', 'type': 'string'},
            'where': {'format': 'binary', 'title': 'Where', 'type': 'string'},
            'why': {'title': 'Why', 'type': 'string'},
        },
        'required': ['when', 'where'],
        'title': 'Meeting',
        'type': 'object',
    }
    """
    