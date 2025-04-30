 {test="skip"}
    from typing import Optional

    from pydantic import BaseModel


    class M1(BaseModel):
        int: Optional[int] = None


    m = M1(int=123)  # errors
    