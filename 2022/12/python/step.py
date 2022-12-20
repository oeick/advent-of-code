from dataclasses import dataclass
from typing import Optional, Self

from coord import Coord


@dataclass
class Step:
    coord: Coord
    value: int
    pre: Optional[Self]

    def get_path_length(self) -> int:
        steps = 0
        current = self
        while current := current.pre:
            steps += 1
        return steps
