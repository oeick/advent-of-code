from typing import NamedTuple, Self


class Coord(NamedTuple):
    x: int
    y: int

    def dist(self, other) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    def neighbors(self) -> set[Self]:
        return {Coord(self.x - 1, self.y),
                Coord(self.x + 1, self.y),
                Coord(self.x, self.y - 1),
                Coord(self.x, self.y + 1)}

    def get_valid_neighbors(self, elevations: list[list[int]]) -> set[Self]:
        return {nb for nb in self.neighbors()
                if self.is_valid_neighbor(nb, elevations)}

    def is_valid_neighbor(self, nb: Self, elevations: list[list[int]]) -> bool:
        return 0 <= nb.x < len(elevations[0]) \
            and 0 <= nb.y < len(elevations) \
            and elevations[nb.y][nb.x] <= elevations[self.y][self.x] + 1
