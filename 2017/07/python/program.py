from dataclasses import dataclass
from typing import Optional


@dataclass
class Program:
    weight: int
    previous: Optional[str]
    subs: Optional[list[str]]
