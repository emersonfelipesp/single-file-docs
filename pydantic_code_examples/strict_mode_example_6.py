
from pydantic import BaseModel, Field, ValidationError


class User(BaseModel):
    name: str
    age: int
    n_pets: int


user = User(name='John', age='42', n_pets='1')
print(user)
#> name='John' age=42 n_pets=1


class AnotherUser(BaseModel):
    name: str
    age: int = Field(strict=True)
    n_pets: int


try:
    anotheruser = AnotherUser(name='John', age='42', n_pets='1')
except ValidationError as e:
    print(e)
    """
    1 validation error for AnotherUser
    age
      Input should be a valid integer [type=int_type, input_value='42', input_type=str]
    """
