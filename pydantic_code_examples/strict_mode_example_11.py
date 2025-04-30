
    from pydantic import BaseModel, ConfigDict, Field


    class User(BaseModel):
        model_config = ConfigDict(strict=True)

        name: str
        age: int = Field(strict=False)
    