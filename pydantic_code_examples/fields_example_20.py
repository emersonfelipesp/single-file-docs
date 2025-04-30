
    from typing import Annotated, Optional

    from pydantic import BaseModel, Field


    class Foo(BaseModel):
        positive: Optional[Annotated[int, Field(gt=0)]]
        # Can error in some cases, not recommended:
        non_negative: Optional[int] = Field(ge=0)
    