from typing import NamedTuple, Final

IMPOSSIBLE_LARGE_DISTANCE: Final[int] = 999_999

WIRE_PATH = list[tuple[str, int]]


class Coords(NamedTuple):
    x: int
    y: int

    def dist(self) -> int:
        return abs(self.x) + abs(self.y)


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        wire1 = calc_wire_coords(parse_wire_path(next(fp)))
        wire2 = calc_wire_coords(parse_wire_path(next(fp)))
    intersection = set(wire1).intersection(set(wire2))
    return (solve_part_1(intersection),
            solve_part_2(wire1, wire2, intersection))


def parse_wire_path(line: str) -> WIRE_PATH:
    return [(w[0], int(w[1:])) for w in line.split(',')]


def solve_part_1(intersection: set[Coords]) -> int:
    shortest_distance = IMPOSSIBLE_LARGE_DISTANCE
    for coords in intersection:
        if coords == (0, 0):
            continue
        shortest_distance = min(coords.dist(), shortest_distance)
    return shortest_distance


def solve_part_2(wire1: list[Coords],
                 wire2: list[Coords],
                 intersection: set[Coords]) -> int:
    fewest = len(wire1) + len(wire2)
    for coord_i in intersection:
        if coord_i == (0, 0):
            continue
        count1 = wire1.index(coord_i)
        count2 = wire2.index(coord_i)
        fewest = min(fewest, count1 + count2)
    return fewest


def calc_wire_coords(wire_path: WIRE_PATH) -> list[Coords]:
    wire_coord = [Coords(0, 0)]
    for direction, length in wire_path:
        wire_coord += get_coords(wire_coord[-1], direction, length)
    return wire_coord


def get_coords(start: Coords, direction: str, length: int) -> list[Coords]:
    match direction:
        case 'U':
            return [Coords(start.x, start.y + n + 1) for n in range(length)]
        case 'R':
            return [Coords(start.x + n + 1, start.y) for n in range(length)]
        case 'D':
            return [Coords(start.x, start.y - n - 1) for n in range(length)]
        case 'L':
            return [Coords(start.x - n - 1, start.y) for n in range(length)]


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
