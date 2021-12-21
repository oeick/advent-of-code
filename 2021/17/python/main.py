import math
import re
from functools import reduce
from math import ceil, floor
from typing import NamedTuple, Optional


class Target(NamedTuple):
    x1: int
    x2: int
    y1: int
    y2: int


def calc_t(v: int, pos: int) -> Optional[float]:
    a, b, c = -1 / 2, 1 / 2 + v, -pos
    s = b ** 2 - 4 * a * c
    solutions = None
    if s >= 0:
        solutions = ((-b - math.sqrt(s)) / (2 * a),
                     (-b + math.sqrt(s)) / (2 * a))
    if solutions is not None:
        return min(t for t in solutions if t >= 0)


def calc_tx_range(vx, x1, x2):
    low = calc_t(vx, x1)
    if low is None:
        return math.inf, -math.inf
    high = calc_t(vx, x2)
    left = math.ceil(low)
    right = math.inf if high is None else math.floor(high)
    return left, right


def calc_distance(v: int) -> int:
    t = max(0, v)
    return round(-0.5 * t ** 2 + (0.5 + v) * t)


def check_ranges_intersect(a: tuple[int, int], b: tuple[int, int]) -> bool:
    return a[0] <= b[1] and a[1] >= b[0] or b[0] <= a[1] and b[1] >= a[0]


def calc_velocities(target: Target) -> set[tuple[int, int]]:
    ts = [(y, ceil(calc_t(y, target.y2)), floor(calc_t(y, target.y1)))
          for y in range(target.y1, 150)]
    ys = {y: (tl, tr) for y, tl, tr in ts if tl <= tr}
    ts = [(x, *calc_tx_range(x, target.x1, target.x2))
          for x in range(target.x2 + 1)]
    xs = {x: (tl, tr) for x, tl, tr in ts if tl <= tr}
    velocities = {(x, y) for y, yr in ys.items() for x, xr in xs.items()
                  if check_ranges_intersect(yr, xr)}
    return velocities


def find_highest_y(velocities: set[tuple[int, int]]) -> int:
    return reduce(max, [calc_distance(y) for _, y in velocities])


def solve(target: Target) -> (int, int):
    velocities = calc_velocities(target)
    return find_highest_y(velocities), len(velocities)


def parse(content: str) -> Target:
    match = re.search(r'x=(\d+)\.\.(\d+), y=(-?\d+)\.\.(-?\d+)', content)
    x1, x2, y1, y2 = match.groups()
    return Target(int(x1), int(x2), int(y1), int(y2))


def main(filename) -> (int, int):
    with open(filename, 'r') as fp:
        content = fp.read()
    return solve(parse(content))


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
