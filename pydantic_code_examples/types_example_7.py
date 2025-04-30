
        from typing import Annotated

        from typing_extensions import TypeAliasType

        from pydantic import BaseModel, Field

        MyAlias = TypeAliasType('MyAlias', Annotated[int, Field(default=1)])


        class Model(BaseModel):
            x: MyAlias  # This is not allowed
        