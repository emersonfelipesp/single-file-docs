
    from pydantic import BaseModel, Field


    class MyModel(BaseModel):
        my_field: int = Field(validation_alias='myValidationAlias')
    