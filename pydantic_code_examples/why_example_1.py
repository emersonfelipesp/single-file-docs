
    from typing import Annotated, Literal

    from annotated_types import Gt

    from pydantic import BaseModel


    class Fruit(BaseModel):
        name: str  # (1)!
        color: Literal['red', 'green']  # (2)!
        weight: Annotated[float, Gt(0)]  # (3)!
        bazam: dict[str, list[tuple[int, bool, float]]]  # (4)!


    print(
        Fruit(
            name='Apple',
            color='red',
            weight=4.2,
            bazam={'foobar': [(1, True, 0.1)]},
        )
    )
    #> name='Apple' color='red' weight=4.2 bazam={'foobar': [(1, True, 0.1)]}
    