
  from typing import Any

  from pydantic import BaseModel, model_validator


  class UserModel(BaseModel):
      username: str

      @model_validator(mode='before')
      @classmethod
      def check_card_number_not_present(cls, data: Any) -> Any:  # (1)!
          if isinstance(data, dict):  # (2)!
              if 'card_number' in data:
                  raise ValueError("'card_number' should not be included")
          return data
  