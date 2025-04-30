
    from datetime import datetime, timezone
    from typing import Any

    from pydantic_core.core_schema import ValidatorFunctionWrapHandler

    from pydantic import BaseModel, field_validator


    class Meeting(BaseModel):
        when: datetime

        @field_validator('when', mode='wrap')
        def when_now(
            cls, input_value: Any, handler: ValidatorFunctionWrapHandler
        ) -> datetime:
            if input_value == 'now':
                return datetime.now()
            when = handler(input_value)
            # in this specific application we know tz naive datetimes are in UTC
            if when.tzinfo is None:
                when = when.replace(tzinfo=timezone.utc)
            return when


    print(Meeting(when='2020-01-01T12:00+01:00'))
    #> when=datetime.datetime(2020, 1, 1, 12, 0, tzinfo=TzInfo(+01:00))
    print(Meeting(when='now'))
    #> when=datetime.datetime(2032, 1, 2, 3, 4, 5, 6)
    print(Meeting(when='2020-01-01T12:00'))
    #> when=datetime.datetime(2020, 1, 1, 12, 0, tzinfo=datetime.timezone.utc)
    