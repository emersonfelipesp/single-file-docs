
  from pydantic import BaseModel


  class Model(BaseModel, frozen=True):
      a: str  # (1)!
  