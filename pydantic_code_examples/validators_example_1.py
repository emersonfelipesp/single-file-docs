
        from typing import Annotated

        from pydantic import AfterValidator, BaseModel, ValidationError


        def is_even(value: int) -> int:
            if value % 2 == 1:
                raise ValueError(f'{value} is not an even number')
            return value  # (1)!


        class Model(BaseModel):
            number: Annotated[int, AfterValidator(is_even)]


        try:
            Model(number=1)
        except ValidationError as err:
            print(err)
            """
            1 validation error for Model
            number
              Value error, 1 is not an even number [type=value_error, input_value=1, input_type=int]
            """
        