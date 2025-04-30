 {test="skip"}
from pydantic import TypeAdapter

adapter = TypeAdapter[str | int](str | int)
...
