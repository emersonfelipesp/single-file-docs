
from typing_extensions import TypedDict

from pydantic import ConfigDict, TypeAdapter


class MyTypedDict(TypedDict):
    x: int

    # or `model_config = ...` for BaseModel
    __pydantic_config__ = ConfigDict(strict=True)


TypeAdapter(MyTypedDict)  # ok
