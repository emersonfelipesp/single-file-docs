
        from typing import Any

        from pydantic import BaseModel, ValidationError, field_validator


        class Model(BaseModel):
            numbers: list[int]

            @field_validator('numbers', mode='before')
            @classmethod
            def ensure_list(cls, value: Any) -> Any:  # (1)!
                if not isinstance(value, list):  # (2)!
                    return [value]
                else:
                    return value


        print(Model(numbers=2))
        #> numbers=[2]
        try:
            Model(numbers='str')
        except ValidationError as err:
            print(err)  # (3)!
            """
            1 validation error for Model
            numbers.0
              Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='str', input_type=str]
            """
        