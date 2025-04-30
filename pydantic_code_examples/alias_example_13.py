
    from pydantic import BaseModel, Field


    class Model(BaseModel):
        my_field: str = Field(validation_alias='my_alias')


    m = Model.model_validate(
        {'my_alias': 'foo'}, by_alias=True, by_name=True  # (1)!
    )
    print(repr(m))
    #> Model(my_field='foo')

    m = Model.model_validate(
        {'my_field': 'foo'}, by_alias=True, by_name=True  # (2)!
    )
    print(repr(m))
    #> Model(my_field='foo')
    