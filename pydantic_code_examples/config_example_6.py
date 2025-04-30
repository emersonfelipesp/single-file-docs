
  from typing_extensions import TypedDict

  from pydantic import ConfigDict, with_config


  @with_config(ConfigDict(str_to_lower=True))
  class Model(TypedDict):
      x: str
  