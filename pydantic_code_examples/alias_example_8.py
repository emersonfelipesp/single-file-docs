
    from pydantic import BaseModel, ConfigDict, Field


    class Model(BaseModel):
        my_field: str = Field(validation_alias='my_alias')

        model_config = ConfigDict(validate_by_alias=False, validate_by_name=True)


    print(repr(Model(my_field='foo')))  # (1)!
    #> Model(my_field='foo')
    