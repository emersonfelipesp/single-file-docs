
            from typing import Annotated

            from pydantic import AfterValidator, BaseModel


            def double_number(value: int) -> int:
                return value * 2


            class Model(BaseModel):
                number: Annotated[int, AfterValidator(double_number)]


            print(Model(number=2))
            #> number=4
            