
    from typing import Annotated

    from pydantic import BaseModel, Field


    class Model(BaseModel):
        int_list: list[Annotated[int, Field(gt=0)]]
        # Valid: [1, 3]
        # Invalid: [-1, 2]
    