
    from pydantic import BaseModel, Field


    class Model(BaseModel):
        my_field: str = Field(validation_alias='my_alias')


    m = Model.model_validate(
        {'my_field': 'foo'}, by_alias=False, by_name=True  # (1)!
    )
    print(repr(m))
    #> Model(my_field='foo')
    