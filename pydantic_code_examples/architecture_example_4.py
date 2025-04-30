 {test="skip" lint="skip"}
    class Model(BaseModel):
        foo: bool = Field(strict=True)

        @field_serializer('foo', mode='plain')
        def serialize_foo(self, value: bool) -> Any:
            ...
    