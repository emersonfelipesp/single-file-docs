
from pydantic import BaseModel, Field, PositiveInt

try:
    # this won't work since `PositiveInt` takes precedence over the
    # constraints defined in `Field`, meaning they're ignored
    class Model(BaseModel):
        foo: PositiveInt = Field(lt=10)

except ValueError as e:
    print(e)


# if you find yourself needing this, an alternative is to declare
# the constraints in `Field` (or you could use `conint()`)
# here both constraints will be enforced:
class ModelB(BaseModel):
    # Here both constraints will be applied and the schema
    # will be generated correctly
    foo: int = Field(gt=0, lt=10)


print(ModelB.model_json_schema())
"""
{
    'properties': {
        'foo': {
            'exclusiveMaximum': 10,
            'exclusiveMinimum': 0,
            'title': 'Foo',
            'type': 'integer',
        }
    },
    'required': ['foo'],
    'title': 'ModelB',
    'type': 'object',
}
"""
