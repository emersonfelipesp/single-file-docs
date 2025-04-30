
from typing import Union

from pydantic import BaseModel


class Model(BaseModel):
    x: Union[int, str]


print(Model(x='1'))
#> x='1'
