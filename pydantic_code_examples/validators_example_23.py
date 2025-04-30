
  from typing import Annotated, Any

  from pydantic_core import PydanticUseDefault

  from pydantic import BaseModel, BeforeValidator


  def default_if_none(value: Any) -> Any:
      if value is None:
          raise PydanticUseDefault()
      return value


  class Model(BaseModel):
      name: Annotated[str, BeforeValidator(default_if_none)] = 'default_name'


  print(Model(name=None))
  #> name='default_name'
  