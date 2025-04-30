
    from pydantic import BaseModel, Field


    class Model(BaseModel):
        my_field: str = Field(validation_alias='my_alias')


    m = Model.model_validate(
        {'my_alias': 'foo'},  # (1)!
        by_alias=True,
        by_name=False,
    )
    print(repr(m))
    #> Model(my_field='foo')
    