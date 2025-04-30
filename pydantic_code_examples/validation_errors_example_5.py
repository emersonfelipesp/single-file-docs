
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: bytes
    model_config = {'val_json_bytes': 'hex'}


try:
    Model(x=b'a')
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'bytes_invalid_encoding'
