from typing import NamedTuple, Self, Iterator

from coord import Coord


class Area(NamedTuple):
    elevations: list[list[int]]
    start: Coord
    end: Coord

    def start_at(self, new_start: Coord) -> Self:
        return Area(self.elevations,
                    new_start,
                    self.end)

    def coordinates(self) -> Iterator:
        for y in range(len(self.elevations)):
            for x in range(len(self.elevations[0])):
                yield x, y
