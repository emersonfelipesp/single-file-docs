
from pydantic import BaseModel, Field, SecretStr


class User(BaseModel):
    id: int
    username: str
    password: SecretStr = Field(exclude=True)


class Transaction(BaseModel):
    id: str
    value: int = Field(exclude=True)


t = Transaction(
    id='1234567890',
    value=9876543210,
)

print(t.model_dump())
#> {'id': '1234567890'}
print(t.model_dump(include={'id': True, 'value': True}))  # (1)!
#> {'id': '1234567890'}
