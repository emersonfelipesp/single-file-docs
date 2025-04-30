
from pydantic import BaseModel


class User(BaseModel):
    name: str
    friends: list['User']


class UserLogin(User):
    password: str


class OuterModel(BaseModel):
    user: User


user = UserLogin(
    name='samuel',
    password='pydantic-pw',
    friends=[UserLogin(name='sebastian', password='fastapi-pw', friends=[])],
)

print(OuterModel(user=user).model_dump(serialize_as_any=True))  # (1)!
"""
{
    'user': {
        'name': 'samuel',
        'friends': [
            {'name': 'sebastian', 'friends': [], 'password': 'fastapi-pw'}
        ],
        'password': 'pydantic-pw',
    }
}
"""

print(OuterModel(user=user).model_dump(serialize_as_any=False))  # (2)!
"""
{'user': {'name': 'samuel', 'friends': [{'name': 'sebastian', 'friends': []}]}}
"""
