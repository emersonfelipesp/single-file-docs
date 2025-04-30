 {lint="skip"}
  import logging
  from typing import Any

  from typing_extensions import Self

  from pydantic import BaseModel, ModelWrapValidatorHandler, ValidationError, model_validator


  class UserModel(BaseModel):
      username: str

      @model_validator(mode='wrap')
      @classmethod
      def log_failed_validation(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
          try:
              return handler(data)
          except ValidationError:
              logging.error('Model %s failed to validate with data %s', cls, data)
              raise
  