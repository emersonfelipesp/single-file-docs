
    from pydantic import BaseModel, Field


    class User(BaseModel):
        name: str = Field(alias='username')


    user = User(username='johndoe')  # (1)!
    