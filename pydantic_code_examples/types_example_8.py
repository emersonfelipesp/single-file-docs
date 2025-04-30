 {requires="3.12" upgrade="skip" lint="skip"}
        from typing import Annotated

        from pydantic import BaseModel, Field

        type MyAlias = Annotated[int, Field(default=1)]


        class Model(BaseModel):
            x: MyAlias  # This is not allowed
        