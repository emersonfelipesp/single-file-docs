 {test="skip"}
    from typing import Any, Generic, Self, TypeVar

    from pydantic import BaseModel, model_validator

    T = TypeVar('T')


    class GenericModel(BaseModel, Generic[T]):
        a: T

        @model_validator(mode='after')
        def validate_after(self: Self) -> Self:
            print('after validator running custom validation...')
            return self


    class Model(BaseModel):
        inner: GenericModel[Any]


    m = Model.model_validate(Model(inner=GenericModel[int](a=1)))
    #> after validator running custom validation...
    #> after validator running custom validation...
    print(repr(m))
    #> Model(inner=GenericModel[Any](a=1))
    