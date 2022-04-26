import re
from math import copysign
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int


class Line(NamedTuple):
    p1: Point
    p2: Point


PATTERN = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')


def get_horizontal_points(line: Line) -> list[Point]:
    return [Point(line.p1.x, y) for y in range(
        min(line.p1.y, line.p2.y), max(line.p1.y, line.p2.y) + 1)]


def get_vertical_points(line: Line) -> list[Point]:
    return [Point(x, line.p1.y) for x in range(
        min(line.p1.x, line.p2.x), max(line.p1.x, line.p2.x) + 1)]


def get_diagonal_points(line: Line) -> list[Point]:
    return [Point(line.p1.x + int(copysign(d, line.p2.x - line.p1.x)),
                  line.p1.y + int(copysign(d, line.p2.y - line.p1.y)))
            for d in range(abs(line.p1.x - line.p2.x) + 1)]


def get_line_points(line: Line) -> list[Point]:
    if line.p1.x == line.p2.x:
        return get_horizontal_points(line)
    elif line.p1.y == line.p2.y:
        return get_vertical_points(line)
    else:
        return get_diagonal_points(line)


def put_points_into_map(line: Line, map: dict):
    points = get_line_points(line)
    for point in points:
        if point not in map:
            map[point] = 1
        else:
            map[point] += 1


def filter_orthogonal(lines: list[Line]) -> list[Line]:
    return [line for line in lines if
            line.p1.x == line.p2.x or line.p1.y == line.p2.y]


def filter_diagonal(lines: list[Line]) -> list[Line]:
    return [line for line in lines if
            line.p1.x != line.p2.x and line.p1.y != line.p2.y]


def get_number_of_overlaps(lines: list[Line]) -> int:
    point_map = {}
    for line in lines:
        put_points_into_map(line, point_map)
    return len([v for v in point_map.values() if v > 1])


def solve(lines: list[Line]) -> (int, int):
    return (
        get_number_of_overlaps(filter_orthogonal(lines)),
        get_number_of_overlaps(lines))


def parse_text(text: str) -> Line:
    match = PATTERN.match(text)
    return Line(Point(int(match[1]), int(match[2])),
                Point(int(match[3]), int(match[4])))


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = [parse_text(line) for line in fp]
    return solve(lines)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
