
from pydantic import UUID5, BaseModel, ValidationError


class Model(BaseModel):
    u: UUID5


try:
    Model(u='a6cc5730-2261-11ee-9c43-2eb5a363657c')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'uuid_version'
