 {test="skip"}
from pydantic import BaseModel, ConstrainedInt


class MyInt(ConstrainedInt):
    ge = 0


class Model(BaseModel):
    x: MyInt
