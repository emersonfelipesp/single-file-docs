
from typing import Annotated

from pydantic import BaseModel, Field

MyInt = Annotated[int, Field(ge=0)]


class Model(BaseModel):
    x: MyInt
