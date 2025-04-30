
from pydantic import BaseModel, PydanticUserError
from pydantic.dataclasses import dataclass

try:

    @dataclass
    class Model(BaseModel):
        bar: str

except PydanticUserError as exc_info:
    assert exc_info.code == 'dataclass-on-model'
