
from pydantic import BaseModel, PydanticUserError, field_validator

try:

    class Model(BaseModel):
        a: int = 1

        @field_validator('a')
        def check_a(self, value):
            return value

except PydanticUserError as exc_info:
    assert exc_info.code == 'validator-instance-method'
