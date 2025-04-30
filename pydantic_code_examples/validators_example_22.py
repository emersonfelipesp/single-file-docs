
  from pydantic import BaseModel, SkipValidation


  class Model(BaseModel):
      names: list[SkipValidation[str]]


  m = Model(names=['foo', 'bar'])
  print(m)
  #> names=['foo', 'bar']

  m = Model(names=['foo', 123])  # (1)!
  print(m)
  #> names=['foo', 123]
  