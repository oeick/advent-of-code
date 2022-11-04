from itertools import count
from typing import Iterator

from light import Light

# reduce MAX_WIDTH to increase performance
# increase MAX_WIDTH, if program fails to find solution
MAX_WIDTH = 100


def main(filename: str) -> tuple[str, int]:
    with open(filename, 'r') as fp:
        lights = [Light.parse(r) for r in fp.read().splitlines()]
    return solve(lights)


def solve(lights: list[Light]) -> tuple[str, int]:
    width_prev = MAX_WIDTH + 1
    for area_str, t in get_lights(lights):
        if (width := len(area_str)) >= width_prev:
            return '\n'.join(''.join(line) for line in result), t - 1
        result = area_str
        width_prev = width


def get_lights(lights: list[Light]) -> Iterator:
    for t in count(0):
        if area_str := area_chars(lights):
            yield area_str, t
        for light in lights:
            light.move()


def area_chars(lights: list[Light]) -> list[list[str]]:
    x1, y1, x2, y2 = get_bounds(lights)
    if x2 - x1 > MAX_WIDTH:
        return []
    area = [['.' for _ in range(x1, x2 + 1)] for _ in range(y1, y2 + 1)]
    for i in lights:
        x, y = i.position
        area[y - y1][x - x1] = '#'
    return area


def get_bounds(lights: list[Light]) -> tuple[int, int, int, int]:
    list_of_all_x = [i.position[0] for i in lights]
    list_of_all_y = [i.position[1] for i in lights]
    x1, x2 = min(list_of_all_x), max(list_of_all_x)
    y1, y2 = min(list_of_all_y), max(list_of_all_y)
    return x1, y1, x2, y2


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
