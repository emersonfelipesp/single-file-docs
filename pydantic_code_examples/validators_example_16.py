
  from pydantic_core import PydanticCustomError

  from pydantic import BaseModel, ValidationError, field_validator


  class Model(BaseModel):
      x: int

      @field_validator('x', mode='after')
      @classmethod
      def validate_x(cls, v: int) -> int:
          if v % 42 == 0:
              raise PydanticCustomError(
                  'the_answer_error',
                  '{number} is the answer!',
                  {'number': v},
              )
          return v


  try:
      Model(x=42 * 2)
  except ValidationError as e:
      print(e)
      """
      1 validation error for Model
      x
        84 is the answer! [type=the_answer_error, input_value=84, input_type=int]
      """
  