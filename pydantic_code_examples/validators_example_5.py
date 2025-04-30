
        from typing import Annotated, Any

        from pydantic import BaseModel, BeforeValidator, ValidationError


        def ensure_list(value: Any) -> Any:  # (1)!
            if not isinstance(value, list):  # (2)!
                return [value]
            else:
                return value


        class Model(BaseModel):
            numbers: Annotated[list[int], BeforeValidator(ensure_list)]


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
        