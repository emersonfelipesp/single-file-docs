
import json

from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    bm: type[BaseModel]


try:
    Model.model_validate_json(json.dumps({'bm': 'not a basemodel class'}))
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'needs_python_object'
