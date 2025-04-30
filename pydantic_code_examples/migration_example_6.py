 {test="skip" lint="skip" upgrade="skip"}
    try:
        from pydantic.v1.fields import ModelField
    except ImportError:
        from pydantic.fields import ModelField
    