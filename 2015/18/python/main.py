import typing

GRID = list[list[str, ...], ...]


class COORDS(typing.NamedTuple):
    x: int
    y: int


def parse_grid(lines: list[str]) -> GRID:
    result = [list(line) for line in lines]
    return result


def get_neighbor_candidates(coords: COORDS) -> list:
    xr = range(coords.x - 1, coords.x + 2)
    yr = range(coords.y - 1, coords.y + 2)
    return [COORDS(x, y) for x in xr for y in yr
            if (x, y) != coords]


def get_neighbor_coords(coords: COORDS, grid: GRID) -> list:
    return [c for c in get_neighbor_candidates(coords)
            if 0 <= c.x < len(grid) and 0 <= c.y < len(grid)]


def count_neighbors(coords: COORDS, grid: GRID) -> int:
    neighbor_coords = get_neighbor_coords(coords, grid)
    return len([c for c in neighbor_coords if grid[c.y][c.x] == '#'])


def calc_next_state(grid: GRID, stucked: list = None) -> GRID:
    next_grid = [['.' for _ in line] for line in grid]
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            nn = count_neighbors(COORDS(x, y), grid)
            if (
                    grid[y][x] == '.' and nn == 3 or
                    grid[y][x] == '#' and 2 <= nn <= 3):
                next_grid[y][x] = '#'
    if stucked:
        for x, y in stucked:
            next_grid[y][x] = '#'
    return next_grid


def calc_nth_state(grid: GRID, n: int, stucked: list = None) -> GRID:
    for _ in range(n):
        grid = calc_next_state(grid, stucked)
    return grid


def count_lights(grid: GRID) -> int:
    return sum(line.count('#') for line in grid)


def solve_part_1(grid: GRID, steps: int) -> int:
    grid = calc_nth_state(grid, steps)
    return count_lights(grid)


def solve_part_2(grid: GRID, steps: int) -> int:
    grid = calc_nth_state(grid, steps, stucked=[
        COORDS(0, 0),
        COORDS(99, 0),
        COORDS(99, 99),
        COORDS(0, 99)
    ])
    return count_lights(grid)


def solve(lines: list[str]) -> (int, int):
    grid = parse_grid(lines)
    return solve_part_1(grid, 100), solve_part_2(grid, 100)


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    return solve(lines)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
