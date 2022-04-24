import math
from typing import SupportsFloat
from coords import Coords


def sign(value: SupportsFloat) -> float:
    return math.copysign(1, value)


def calc_distance(coords: Coords) -> int:
    x, y = coords
    if sign(x) == sign(y):
        distance = abs(x + y)
    else:
        distance = max(abs(x), abs(y))
    return distance


def parse_steps(steps: list[str]) -> list[Coords]:
    step_to_coords_map = {'n': Coords(0, 1),
                          'ne': Coords(1, 0),
                          'se': Coords(1, -1),
                          's': Coords(0, -1),
                          'sw': Coords(-1, 0),
                          'nw': Coords(-1, 1)}
    return [step_to_coords_map[s] for s in steps]


def solve(steps: list[str]) -> (int, int):
    current = Coords(0, 0)
    d_max = 0
    for step in parse_steps(steps):
        current += step
        d = calc_distance(current)
        d_max = max(d, d_max)
    return calc_distance(current), d_max


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        steps = fp.read().split(',')
    return solve(steps)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
