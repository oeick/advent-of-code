from math import prod
from typing import Iterator

MAP = list[list[int]]
BASIN = set[tuple[int, int]]


def get_sizes_of_the_three_largest_basins(basins: list[BASIN]) -> list[int]:
    return [len(b) for b in sorted(basins, key=len)[-3:]]


class Solver:
    heightmap: MAP

    def __init__(self, heightmap: MAP):
        self.heightmap = heightmap

    def coordinates(self) -> Iterator[tuple[int, int]]:
        for x in range(len(self.heightmap[0])):
            for y in range(len(self.heightmap)):
                yield x, y

    def is_inside(self, x: int, y: int) -> bool:
        x_size, y_size = len(self.heightmap[0]), len(self.heightmap)
        return 0 <= x < x_size and 0 <= y < y_size

    def neighbors(self, x: int, y: int) -> Iterator[tuple[int, int]]:
        for xn, yn in [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]:
            if self.is_inside(xn, yn):
                yield xn, yn

    def low_points(self) -> Iterator[tuple[int, int]]:
        for x, y in self.coordinates():
            if all(self.heightmap[yn][xn] > self.heightmap[y][x]
                   for xn, yn in self.neighbors(x, y)):
                yield x, y

    def sum_risk_levels(self) -> int:
        return sum(1 + self.heightmap[y][x] for x, y in self.low_points())

    def get_basin(self, x: int, y: int) -> BASIN:
        basin = {(x, y)}
        candidates = {c for c in self.neighbors(x, y)}
        while candidates:
            xc, yc = candidates.pop()
            if self.heightmap[yc][xc] < 9:
                basin.add((xc, yc))
                candidates |= {c for c in self.neighbors(xc, yc)
                               if c not in basin}
        return basin

    def get_all_basins(self) -> list[BASIN]:
        return [self.get_basin(x, y) for x, y in self.low_points()]

    def multiply_sizes_of_three_largest_basins(self) -> int:
        return prod(get_sizes_of_the_three_largest_basins(
            self.get_all_basins()))


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = [[int(n) for n in line]
                 for line in fp.read().splitlines()]
    solver = Solver(lines)
    return (
        solver.sum_risk_levels(),
        solver.multiply_sizes_of_three_largest_basins())


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
