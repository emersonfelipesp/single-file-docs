
        from typing import Annotated, Any

        from pydantic import BaseModel, PlainValidator


        def val_number(value: Any) -> Any:
            if isinstance(value, int):
                return value * 2
            else:
                return value


        class Model(BaseModel):
            number: Annotated[int, PlainValidator(val_number)]


        print(Model(number=4))
        #> number=8
        print(Model(number='invalid'))  # (1)!
        #> number='invalid'
        