 {lint="skip" test="skip"}
    some_field: Union[...] = Field(discriminator='my_discriminator')
    some_field: Annotated[Union[...], Field(discriminator='my_discriminator')]
    