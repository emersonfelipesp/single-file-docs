
    from typing import Any, Generic, TypeVar

    from pydantic import BaseModel

    T = TypeVar('T')


    class GenericModel(BaseModel, Generic[T]):
        a: T


    class Model(BaseModel):
        inner: GenericModel[Any]


    print(repr(Model.model_validate(Model(inner=GenericModel[int](a=1)))))
    #> Model(inner=GenericModel[Any](a=1))
    