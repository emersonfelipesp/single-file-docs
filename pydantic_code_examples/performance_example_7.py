 {test="skip"}
    from timeit import timeit

    from typing_extensions import TypedDict

    from pydantic import BaseModel, TypeAdapter


    class A(TypedDict):
        a: str
        b: int


    class TypedModel(TypedDict):
        a: A


    class B(BaseModel):
        a: str
        b: int


    class Model(BaseModel):
        b: B


    ta = TypeAdapter(TypedModel)
    result1 = timeit(
        lambda: ta.validate_python({'a': {'a': 'a', 'b': 2}}), number=10000
    )
    result2 = timeit(
        lambda: Model.model_validate({'b': {'a': 'a', 'b': 2}}), number=10000
    )
    print(result2 / result1)
    