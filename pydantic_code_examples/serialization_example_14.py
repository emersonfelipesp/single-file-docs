
from typing import Any

from pydantic import BaseModel, SecretStr


class MyBaseModel(BaseModel):
    def model_dump(self, **kwargs) -> dict[str, Any]:
        return super().model_dump(serialize_as_any=True, **kwargs)

    def model_dump_json(self, **kwargs) -> str:
        return super().model_dump_json(serialize_as_any=True, **kwargs)


class User(MyBaseModel):
    name: str


class UserInfo(User):
    password: SecretStr


class OuterModel(MyBaseModel):
    user: User


u = OuterModel(user=UserInfo(name='John', password='secret_pw'))
print(u.model_dump_json())  # (1)!
#> {"user":{"name":"John","password":"**********"}}
