
from pydantic import BaseModel, PydanticUserError, field_validator

try:

    class Model(BaseModel):
        a: str

        @field_validator
        def checker(cls, v):
            return v

except PydanticUserError as exc_info:
    assert exc_info.code == 'validator-no-fields'
