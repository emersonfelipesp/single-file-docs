
        from pydantic import BaseModel


        class Model(BaseModel):
            a: int


        m = Model(a=0)
        # note: setting `validate_assignment` to `True` in the config can prevent this kind of misbehavior.
        m.a = 'not an int'

        # doesn't raise a validation error even though m is invalid
        m2 = Model.model_validate(m)
        