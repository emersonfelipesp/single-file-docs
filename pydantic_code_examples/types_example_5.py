
    from typing import Annotated

    from annotated_types import Gt
    from typing_extensions import TypeAliasType

    from pydantic import BaseModel

    PositiveIntList = TypeAliasType('PositiveIntList', list[Annotated[int, Gt(0)]])


    class Model(BaseModel):
        x: PositiveIntList
        y: PositiveIntList


    print(Model.model_json_schema())  # (1)!
    """
    {
        '$defs': {
            'PositiveIntList': {
                'items': {'exclusiveMinimum': 0, 'type': 'integer'},
                'type': 'array',
            }
        },
        'properties': {
            'x': {'$ref': '#/$defs/PositiveIntList'},
            'y': {'$ref': '#/$defs/PositiveIntList'},
        },
        'required': ['x', 'y'],
        'title': 'Model',
        'type': 'object',
    }
    """
    