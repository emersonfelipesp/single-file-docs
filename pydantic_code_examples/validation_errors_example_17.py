
import json
from datetime import date

from pydantic import BaseModel, Field, ValidationError


class Model(BaseModel):
    x: date = Field(strict=True)


try:
    Model.model_validate_json(json.dumps({'x': '1'}))
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'date_parsing'
