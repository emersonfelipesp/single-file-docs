 {test="skip" lint="skip"}
    class Model(BaseModel):
        field_bad: Annotated[int, Field(deprecated=True)] | None = None  # (1)!
        field_ok: Annotated[int | None, Field(deprecated=True)] = None  # (2)!
    