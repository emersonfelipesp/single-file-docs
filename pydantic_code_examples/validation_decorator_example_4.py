
    from typing_extensions import TypedDict, Unpack

    from pydantic import validate_call


    class Point(TypedDict):
        x: int
        y: int


    @validate_call
    def add_coords(**kwargs: Unpack[Point]) -> int:
        return kwargs['x'] + kwargs['y']


    add_coords(x=1, y=2)
    