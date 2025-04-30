 {test="skip" lint="skip" upgrade="skip"}
from pydantic import SerializerFunctionWrapHandler, SerializationInfo, model_serializer

# an instance method with the default mode or `mode='plain'`
@model_serializer  # or model_serializer(mode='plain')
def mod_ser(self, info: SerializationInfo): ...

# an instance method with `mode='wrap'`
@model_serializer(mode='wrap')
def mod_ser(self, handler: SerializerFunctionWrapHandler, info: SerializationInfo):

# For all of these, you can also choose to omit the `info` argument, for example:
@model_serializer(mode='plain')
def mod_ser(self): ...

@model_serializer(mode='wrap')
def mod_ser(self, handler: SerializerFunctionWrapHandler): ...
