from typing import Optional

from area import Area
from coord import Coord
from step import Step


def main(filename: str) -> tuple[int, int]:
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    area = parse_area(lines)
    return solve_part_1(area), solve_part_2(area)


def parse_area(lines: list[str]) -> Area:
    elevations: list[list[int]] = list()
    start = None
    end = None
    for y in range(len(lines)):
        elevations.append(list())
        for x in range(len(lines[0])):
            elevations[y].append(parse_height(lines[y][x]))
            match lines[y][x]:
                case 'S':
                    start = Coord(x, y)
                case 'E':
                    end = Coord(x, y)
    return Area(elevations, start, end)


def parse_height(symbol: str) -> int:
    match symbol:
        case 'S':
            return 0
        case 'E':
            return ord('z') - ord('a')
        case _:
            return ord(symbol) - ord('a')


def solve_part_1(area: Area) -> int:
    return find_shortest_route(area).get_path_length()


def solve_part_2(area: Area) -> int:
    shortest = 999
    for x, y in area.coordinates():
        if area.elevations[y][x] == 0:
            route = find_shortest_route(area.start_at(Coord(x, y)))
            if route:
                shortest = min(shortest, route.get_path_length())
    return shortest


def find_shortest_route(area: Area) -> Optional[Step]:
    current = Step(area.start, area.start.dist(area.end), None)
    open_list: list[Step] = list()
    closed_list: set[Coord] = set()
    while current.coord != area.end:
        closed_list.add(current.coord)
        expand_steps(current, open_list, closed_list, area.elevations)
        if not open_list:
            return None
        current = open_list.pop()
    return current


def expand_steps(current: Step,
                 open_list: list[Step],
                 closed_list: set[Coord],
                 elevations: list[list[int]]):
    for nb in current.coord.get_valid_neighbors(elevations):
        if nb in closed_list:
            continue
        new_value = current.value + 1
        already_open = [s for s in open_list if s.coord == nb]
        if already_open:
            if new_value <= already_open[0].value:
                continue
            else:
                already_open[0].value = new_value
                already_open[0].pre = current
        else:
            new_step = Step(nb, new_value, current)
            put_into_sorted_list(new_step, open_list)


def put_into_sorted_list(new_step: Step, open_list: list[Step]):
    for i, s in enumerate(open_list):
        if new_step.value > s.value:
            open_list.insert(i, new_step)
            break
    else:
        open_list.append(new_step)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
