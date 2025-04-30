 {test="skip"}
    from typing import Optional

    from pydantic import BaseModel


    class Boo(BaseModel):
        int: Optional[int] = None


    m = Boo(int=123)  # Will fail to validate.
    