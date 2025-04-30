
  from pydantic import BaseModel, ConfigDict, ValidationError


  class Model(BaseModel):
      model_config = ConfigDict(str_max_length=5)  # (1)!

      v: str


  try:
      m = Model(v='abcdef')
  except ValidationError as e:
      print(e)
      """
      1 validation error for Model
      v
        String should have at most 5 characters [type=string_too_long, input_value='abcdef', input_type=str]
      """
  