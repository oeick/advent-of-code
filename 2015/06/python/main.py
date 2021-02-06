import re
from collections import namedtuple

GRID_SIZE = 1000
PATTERN = re.compile(r'.* (\d+),(\d+) through (\d+),(\d+).*')

Rectangle = namedtuple('Rect', ['x1', 'y1', 'x2', 'y2'])


class Lights:

    grid: list[list[int]]

    def __init__(self, size: int):
        self.grid = [[0 for _ in range(size)] for _ in range(size)]

    def turn(self, rect: Rectangle, state: int):
        for x in range(rect.x1, rect.x2+1):
            for y in range(rect.y1, rect.y2+1):
                self.grid[x][y] = state

    def toggle(self, rect: Rectangle):
        for x in range(rect.x1, rect.x2+1):
            for y in range(rect.y1, rect.y2+1):
                self.grid[x][y] = 0 if self.grid[x][y] == 1 else 1

    def increase(self, rect: Rectangle, value: int):
        for x in range(rect.x1, rect.x2+1):
            for y in range(rect.y1, rect.y2+1):
                self.grid[x][y] = self.grid[x][y] + value

    def decrease(self, rect: Rectangle):
        for x in range(rect.x1, rect.x2+1):
            for y in range(rect.y1, rect.y2+1):
                self.grid[x][y] = max(self.grid[x][y] - 1, 0)

    def count_lit(self):
        return sum(sum(g) for g in self.grid)

    def total_brightness(self):
        return self.count_lit()


def parse_rectangle(string: str) -> Rectangle:
    match = re.match(PATTERN, string)
    return Rectangle(int(match[1]),
                     int(match[2]),
                     int(match[3]),
                     int(match[4]))


def solve_part_1(lines: list[str]) -> int:
    lights = Lights(GRID_SIZE)
    for line in lines:
        rectangle = parse_rectangle(line)
        if line[6] == 'f':
            lights.turn(rectangle, 0)
        elif line[6] == 'n':
            lights.turn(rectangle, 1)
        elif line[6] == ' ':
            lights.toggle(rectangle)
    return lights.count_lit()


def solve_part_2(lines: list[str]) -> int:
    lights = Lights(GRID_SIZE)
    for line in lines:
        rectangle = parse_rectangle(line)
        if line[6] == 'f':
            lights.decrease(rectangle)
        elif line[6] == 'n':
            lights.increase(rectangle, 1)
        elif line[6] == ' ':
            lights.increase(rectangle, 2)
    return lights.total_brightness()


def main(filename: str) -> (int, int):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return (solve_part_1(lines),
            solve_part_2(lines))


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
