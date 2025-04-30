 {lint="skip"}
    from dataclasses import dataclass

    from pydantic import BaseModel


    @dataclass
    class Foo:
        # `a` and `b` shouldn't resolve:
        a: 'Model'
        b: 'Inner'


    def func():
        Inner = int

        class Model(BaseModel):
            foo: Foo

        Model.__pydantic_complete__
        #> True, should be False.
    