 {requires="3.12" upgrade="skip" lint="skip"}
    from pydantic import TypeAdapter

    type Json = dict[str, Json] | list[Json] | str | int | float | bool | None  # (1)!

    ta = TypeAdapter(Json)
    print(ta.json_schema())
    """
    {
        '$defs': {
            'Json': {
                'anyOf': [
                    {
                        'additionalProperties': {'$ref': '#/$defs/Json'},
                        'type': 'object',
                    },
                    {'items': {'$ref': '#/$defs/Json'}, 'type': 'array'},
                    {'type': 'string'},
                    {'type': 'integer'},
                    {'type': 'number'},
                    {'type': 'boolean'},
                    {'type': 'null'},
                ]
            }
        },
        '$ref': '#/$defs/Json',
    }
    """
    