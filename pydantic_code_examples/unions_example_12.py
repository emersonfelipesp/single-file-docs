
from typing import Annotated, Union

from pydantic import AfterValidator, Tag, TypeAdapter, ValidationError

DoubledList = Annotated[list[int], AfterValidator(lambda x: x * 2)]
StringsMap = dict[str, str]


# Not using any `Tag`s for each union case, the errors are not so nice to look at
adapter = TypeAdapter(Union[DoubledList, StringsMap])

try:
    adapter.validate_python(['a'])
except ValidationError as exc_info:
    print(exc_info)
    """
    2 validation errors for union[function-after[<lambda>(), list[int]],dict[str,str]]
    function-after[<lambda>(), list[int]].0
      Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='a', input_type=str]
    dict[str,str]
      Input should be a valid dictionary [type=dict_type, input_value=['a'], input_type=list]
    """

tag_adapter = TypeAdapter(
    Union[
        Annotated[DoubledList, Tag('DoubledList')],
        Annotated[StringsMap, Tag('StringsMap')],
    ]
)

try:
    tag_adapter.validate_python(['a'])
except ValidationError as exc_info:
    print(exc_info)
    """
    2 validation errors for union[DoubledList,StringsMap]
    DoubledList.0
      Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='a', input_type=str]
    StringsMap
      Input should be a valid dictionary [type=dict_type, input_value=['a'], input_type=list]
    """
