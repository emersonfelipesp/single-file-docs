
  from dataclasses import dataclass

  from pydantic import ConfigDict


  @dataclass
  class User:
      __pydantic_config__ = ConfigDict(strict=True)

      id: int
      name: str = 'John Doe'
  