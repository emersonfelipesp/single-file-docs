
    from pydantic import BaseModel


    class CompletedModel(BaseModel):
        s: str
        done: bool = False
    