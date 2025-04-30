
            from pydantic import BaseModel, field_validator


            class Model(BaseModel):
                number: int

                @field_validator('number', mode='after')  # (1)!
                @classmethod
                def double_number(cls, value: int) -> int:
                    return value * 2


            print(Model(number=2))
            #> number=4
            