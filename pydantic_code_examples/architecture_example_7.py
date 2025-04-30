
from pydantic import BaseModel


class Model(BaseModel):
    foo: int


model = Model.model_validate({'foo': 1})  # (1)!
dumped = model.model_dump()  # (2)!
