from typing import Iterator, NamedTuple

from knot_hash import calc_hash


class Coords(NamedTuple):
    row: int
    col: int


def hex2bin(hex: str) -> str:
    return ''.join(['{:04b}'.format(int(c, 16)) for c in hex])


def build_grid(key: str) -> list[str]:
    return [hex2bin(calc_hash(range(256), f'{key}-{i}')) for i in range(128)]


def solve_part_1(grid: list[str]) -> int:
    return sum(row.count('1') for row in grid)


def neighbor_coords(pos: Coords) -> Iterator:
    row, col = pos
    for nrow, ncol in [(row - 1, col), (row, col - 1),
                       (row, col + 1), (row + 1, col)]:
        yield Coords(nrow, ncol)


def get_neighbors(pos: Coords, grid: list[str]) -> set[Coords]:
    return {Coords(r, c) for r, c in neighbor_coords(pos)
            if 0 <= r < len(grid)
            and 0 <= c < len(grid[r])
            and grid[r][c] == '1'}


def find_group(pos: Coords, grid: list[str]) -> set[Coords]:
    group = {pos, }
    newbies = {pos, }
    while newbies:
        newbie = newbies.pop()
        neighbors = get_neighbors(newbie, grid)
        newbies |= neighbors - group
        group |= neighbors
    return group


def squares(grid: list[str]) -> Iterator:
    for col in range(len(grid[0])):
        for row in range(len(grid)):
            yield Coords(row, col)


def find_groups(grid: list[str]) -> list[set[Coords]]:
    groups = []
    for square in squares(grid):
        row, col = square
        if grid[row][col] == '1' and not any(square in g for g in groups):
            groups.append(find_group(square, grid))
    return groups


def solve_part_2(grid: list[str]) -> int:
    return len(find_groups(grid))


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        key = fp.read()
    grid = build_grid(key)
    return solve_part_1(grid), solve_part_2(grid)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
