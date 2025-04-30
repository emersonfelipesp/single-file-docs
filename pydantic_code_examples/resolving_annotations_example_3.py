 {test="skip" lint="skip"}
# module1.py:
type MyType = int

class Base:
    f1: 'MyType'

# module2.py:
from pydantic import BaseModel

from module1 import Base

type MyType = str


def inner() -> None:
    type InnerType = bool

    class Model(BaseModel, Base):
        type LocalType = bytes

        f2: 'MyType'
        f3: 'InnerType'
        f4: 'LocalType'
        f5: 'UnknownType'

    type InnerType2 = complex
