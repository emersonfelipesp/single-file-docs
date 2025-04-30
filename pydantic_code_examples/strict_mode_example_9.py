
from typing import Annotated

from pydantic import BaseModel, Strict, ValidationError


class User(BaseModel):
    name: str
    age: int
    is_active: Annotated[bool, Strict()]


User(name='David', age=33, is_active=True)
try:
    User(name='David', age=33, is_active='True')
except ValidationError as exc:
    print(exc)
    """
    1 validation error for User
    is_active
      Input should be a valid boolean [type=bool_type, input_value='True', input_type=str]
    """
