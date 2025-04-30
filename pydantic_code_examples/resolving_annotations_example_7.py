 {lint="skip"}
from pydantic import BaseModel


class Foo(BaseModel):
    f: 'MyType'


Foo.__pydantic_core_schema__
#> <pydantic._internal._mock_val_ser.MockCoreSchema object at 0x73cd0d9e6d00>
