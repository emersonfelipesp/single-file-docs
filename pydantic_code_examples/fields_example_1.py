
from pydantic import BaseModel, Field


class Model(BaseModel):
    name: str = Field(frozen=True)
