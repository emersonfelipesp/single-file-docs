
from pydantic import BaseModel, model_serializer


class Model(BaseModel):
    x: str

    @model_serializer
    def ser_model(self) -> str:
        return self.x


print(Model(x='not a dict').model_dump())
#> not a dict
