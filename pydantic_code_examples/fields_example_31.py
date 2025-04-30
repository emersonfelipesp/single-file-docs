 {test="skip"}
import importlib.metadata
from typing import Annotated, deprecated

from packaging.version import Version

from pydantic import BaseModel, Field

if Version(importlib.metadata.version('typing_extensions')) >= Version('4.9'):

    class Model(BaseModel):
        deprecated_field: Annotated[int, deprecated('This is deprecated')]

        # Or explicitly using `Field`:
        alt_form: Annotated[
            int, Field(deprecated=deprecated('This is deprecated'))
        ]
