from __future__ import annotations

from typing import NamedTuple


class Coords(NamedTuple):
    x: int
    y: int

    def __add__(self, other) -> Coords:
        return Coords(self.x + other.x, self.y + other.y)
