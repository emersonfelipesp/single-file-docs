
from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    name: str


class Parent(BaseModel):
    user: User

    model_config = ConfigDict(str_max_length=2)


print(Parent(user={'name': 'John Doe'}))
#> user=User(name='John Doe')
