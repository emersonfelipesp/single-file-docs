
from pydantic import BaseModel


class Model(BaseModel):
    items: list[int]  # (1)!


print(Model(items=(1, 2, 3)))
#> items=[1, 2, 3]
