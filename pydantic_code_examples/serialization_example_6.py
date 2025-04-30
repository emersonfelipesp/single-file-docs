
from typing import Annotated, Any

from pydantic import BaseModel, SerializerFunctionWrapHandler
from pydantic.functional_serializers import WrapSerializer


def ser_wrap(v: Any, nxt: SerializerFunctionWrapHandler) -> str:
    return f'{nxt(v + 1):,}'


FancyInt = Annotated[int, WrapSerializer(ser_wrap, when_used='json')]


class MyModel(BaseModel):
    x: FancyInt


print(MyModel(x=1234).model_dump())
#> {'x': 1234}

print(MyModel(x=1234).model_dump(mode='json'))
#> {'x': '1,235'}
