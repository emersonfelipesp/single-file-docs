 {title="Old way"}
from pydantic import BaseModel, PydanticUserError

try:

    class Model(BaseModel):
        @classmethod
        def __modify_schema__(cls, field_schema):
            field_schema.update(examples=['example'])

except PydanticUserError as exc_info:
    assert exc_info.code == 'custom-json-schema'
