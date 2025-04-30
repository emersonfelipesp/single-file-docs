
from pydantic import BaseModel, Field


class Model(BaseModel):
    foo: bool = Field(strict=True)
