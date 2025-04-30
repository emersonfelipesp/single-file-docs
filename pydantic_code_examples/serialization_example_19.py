
from typing import Optional

from pydantic import BaseModel, Field


class Person(BaseModel):
    name: str
    age: Optional[int] = Field(None, exclude=False)


person = Person(name='Jeremy')

print(person.model_dump())
#> {'name': 'Jeremy', 'age': None}
print(person.model_dump(exclude_none=True))  # (1)!
#> {'name': 'Jeremy'}
print(person.model_dump(exclude_unset=True))  # (2)!
#> {'name': 'Jeremy'}
print(person.model_dump(exclude_defaults=True))  # (3)!
#> {'name': 'Jeremy'}
