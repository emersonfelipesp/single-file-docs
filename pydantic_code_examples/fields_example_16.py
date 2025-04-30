
    from typing import Annotated

    from pydantic import BaseModel, ConfigDict, Field


    class User(BaseModel):
        model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

        name: Annotated[str, Field(alias='username')]


    user = User(name='johndoe')  # (1)!
    user = User(username='johndoe')  # (2)!
    