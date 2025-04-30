
from pydantic import BaseModel, ConfigDict, Field, PydanticUserError

try:

    class Model(BaseModel):
        a: int = Field(alias='A')

        model_config = ConfigDict(
            validate_by_alias=False, validate_by_name=False
        )

except PydanticUserError as exc_info:
    assert exc_info.code == 'validate-by-alias-and-name-false'
