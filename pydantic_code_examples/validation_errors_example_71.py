
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: list['Model']


d = {'x': []}
d['x'].append(d)
try:
    Model(**d)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'recursion_loop'
