 {test="skip" lint="skip"}
class Model(BaseModel):
    a: int = 1


Model(unrelated=2)
