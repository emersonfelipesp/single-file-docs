 {test="skip" lint="skip"}
type MyType = int

Foo.model_rebuild()
Foo.__pydantic_core_schema__
#> {'type': 'model', 'schema': {...}, ...}
