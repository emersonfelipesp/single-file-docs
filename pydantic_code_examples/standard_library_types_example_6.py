
from decimal import Decimal
from typing import Annotated

from pydantic import BaseModel, PlainSerializer


class Model(BaseModel):
    x: Decimal
    y: Annotated[
        Decimal,
        PlainSerializer(
            lambda x: float(x), return_type=float, when_used='json'
        ),
    ]


my_model = Model(x=Decimal('1.1'), y=Decimal('2.1'))

print(my_model.model_dump())  # (1)!
#> {'x': Decimal('1.1'), 'y': Decimal('2.1')}
print(my_model.model_dump(mode='json'))  # (2)!
#> {'x': '1.1', 'y': 2.1}
print(my_model.model_dump_json())  # (3)!
#> {"x":"1.1","y":2.1}
