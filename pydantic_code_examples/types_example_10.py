 {requires="3.12" upgrade="skip" lint="skip"}
        from typing import Annotated, TypeVar

        from annotated_types import Len

        type ShortList[T] = Annotated[list[T], Len(max_length=4)]
        