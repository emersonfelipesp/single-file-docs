 {test="skip" lint="skip"}
  from annotated_types import Gt

  PositiveInt = Annotated[int, Gt(0)]
  