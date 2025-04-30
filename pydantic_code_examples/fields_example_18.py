
    from pydantic import BaseModel, Field


    class MyModel(BaseModel):
        my_field: int = Field(
            alias='myValidationAlias',
            serialization_alias='my_field',
        )


    m = MyModel(myValidationAlias=1)
    print(m.model_dump(by_alias=True))
    #> {'my_field': 1}
    