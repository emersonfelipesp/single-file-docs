
from typing import Annotated, Union

from pydantic import BaseModel, Discriminator, PydanticUserError, Tag


def model_x_discriminator(v):
    if isinstance(v, str):
        return 'str'
    if isinstance(v, (dict, BaseModel)):
        return 'model'


# tag missing for both union choices
try:

    class DiscriminatedModel(BaseModel):
        x: Annotated[
            Union[str, 'DiscriminatedModel'],
            Discriminator(model_x_discriminator),
        ]

except PydanticUserError as exc_info:
    assert exc_info.code == 'callable-discriminator-no-tag'

# tag missing for `'DiscriminatedModel'` union choice
try:

    class DiscriminatedModel(BaseModel):
        x: Annotated[
            Union[Annotated[str, Tag('str')], 'DiscriminatedModel'],
            Discriminator(model_x_discriminator),
        ]

except PydanticUserError as exc_info:
    assert exc_info.code == 'callable-discriminator-no-tag'

# tag missing for `str` union choice
try:

    class DiscriminatedModel(BaseModel):
        x: Annotated[
            Union[str, Annotated['DiscriminatedModel', Tag('model')]],
            Discriminator(model_x_discriminator),
        ]

except PydanticUserError as exc_info:
    assert exc_info.code == 'callable-discriminator-no-tag'
