from itertools import combinations


def solve_part_1(rows: list[list[int]]) -> int:
    return sum(max(row) - min(row) for row in rows)


def solve_part_2(rows: list[list[int]]) -> int:
    return sum([max(c) // min(c) for c in combinations(row, 2)
                if max(c) % min(c) == 0][0] for row in rows)


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        rows = [[int(d) for d in row.split()]
                for row in fp.read().splitlines()]
    return solve_part_1(rows), solve_part_2(rows)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
