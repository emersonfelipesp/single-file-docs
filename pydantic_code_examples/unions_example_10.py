 {lint="skip" test="skip"}
    type_adapter = TypeAdapter(Pet)

    pet = type_adapter.validate_python(
        {'pet_type': 'cat', 'color': 'black', 'black_name': 'felix'}
    )
    print(repr(pet))
    #> BlackCat(pet_type='cat', color='black', black_name='felix')
    