
    from pydantic import BaseModel, ConfigDict, Field


    class User(BaseModel):
        model_config = ConfigDict(validate_by_name=True)

        name: str = Field(alias='username')


    user = User(name='johndoe')  # (1)!
    