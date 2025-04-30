 {test="skip" lint="skip"}
    def func():
        A = int

        class Model(BaseModel):
            f: 'A | Forward'

        return Model


    Model = func()

    Model.model_rebuild(_types_namespace={'Forward': str})
    # pydantic.errors.PydanticUndefinedAnnotation: name 'A' is not defined
    