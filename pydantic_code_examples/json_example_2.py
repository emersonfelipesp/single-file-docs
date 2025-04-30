
from pydantic_core import from_json

partial_json_data = '["aa", "bb", "c'  # (1)!

try:
    result = from_json(partial_json_data, allow_partial=False)
except ValueError as e:
    print(e)  # (2)!
    #> EOF while parsing a string at line 1 column 15

result = from_json(partial_json_data, allow_partial=True)
print(result)  # (3)!
#> ['aa', 'bb']
