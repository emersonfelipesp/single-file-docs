 {lint="skip" test="skip"}
    class Model(BaseModel):
        name: str = Field(..., frozen=True)
    