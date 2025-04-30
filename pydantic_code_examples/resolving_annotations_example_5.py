
from dataclasses import dataclass

from pydantic import BaseModel


@dataclass
class Foo:
    a: 'Bar | None' = None


class Bar(BaseModel):
    b: Foo
