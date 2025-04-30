 {lint="skip" test="skip"}
    some_field: Union[...] = Field(discriminator=Discriminator(...))
    some_field: Annotated[Union[...], Discriminator(...)]
    some_field: Annotated[Union[...], Field(discriminator=Discriminator(...))]
    