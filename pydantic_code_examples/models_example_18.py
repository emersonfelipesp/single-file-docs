
        from pydantic import BaseModel, ConfigDict, ValidationError


        class Model(BaseModel):
            a: int

            model_config = ConfigDict(revalidate_instances='always')


        m = Model(a=0)
        # note: setting `validate_assignment` to `True` in the config can prevent this kind of misbehavior.
        m.a = 'not an int'

        try:
            m2 = Model.model_validate(m)
        except ValidationError as e:
            print(e)
            """
            1 validation error for Model
            a
              Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='not an int', input_type=str]
            """
        