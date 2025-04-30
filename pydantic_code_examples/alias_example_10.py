
from pydantic import BaseModel, ConfigDict, Field


class Model(BaseModel):
    my_field: str = Field(serialization_alias='my_alias')

    model_config = ConfigDict(serialize_by_alias=True)


m = Model(my_field='foo')
print(m.model_dump())  # (1)!
#> {'my_alias': 'foo'}
