
    from datetime import datetime

    from pydantic import BaseModel


    class Meeting(BaseModel):
        when: datetime
        where: bytes
        why: str = 'No idea'


    m = Meeting(when='2020-01-01T12:00', where='home')
    print(m.model_dump(exclude_unset=True))
    #> {'when': datetime.datetime(2020, 1, 1, 12, 0), 'where': b'home'}
    print(m.model_dump(exclude={'where'}, mode='json'))
    #> {'when': '2020-01-01T12:00:00', 'why': 'No idea'}
    print(m.model_dump_json(exclude_defaults=True))
    #> {"when":"2020-01-01T12:00:00","where":"home"}
    