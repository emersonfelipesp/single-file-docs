
from typing import Annotated

from pydantic import BaseModel
from pydantic.functional_serializers import PlainSerializer

FancyInt = Annotated[
    int, PlainSerializer(lambda x: f'{x:,}', return_type=str, when_used='json')
]


class MyModel(BaseModel):
    x: FancyInt


print(MyModel(x=1234).model_dump())
#> {'x': 1234}

print(MyModel(x=1234).model_dump(mode='json'))
#> {'x': '1,234'}
