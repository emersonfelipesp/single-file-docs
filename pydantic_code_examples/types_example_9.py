
        from typing import Annotated, TypeVar

        from annotated_types import Len
        from typing_extensions import TypeAliasType

        T = TypeVar('T')

        ShortList = TypeAliasType(
            'ShortList', Annotated[list[T], Len(max_length=4)], type_params=(T,)
        )
        