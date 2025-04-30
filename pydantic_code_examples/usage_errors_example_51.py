
from pydantic import BaseModel, PydanticUserError

try:

    class Model(BaseModel):
        model_config: str

except PydanticUserError as exc_info:
    assert exc_info.code == 'model-config-invalid-field-name'
