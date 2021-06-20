def validate(sides: tuple[int, ...]):
    return sorted(sides)[-1] < sum(sorted(sides)[:-1])


def solve_part_1(side_lengths: list[tuple[int, ...]]) -> int:
    return len([t for t in side_lengths if validate(t)])


def get_triangle(side_lengths: list[tuple[int, ...]]) -> tuple[int, ...]:
    for row in range(0, len(side_lengths), 3):
        for column in range(3):
            yield tuple(v[column] for v in side_lengths[row:row + 3])


def solve_part_2(side_lengths: list[tuple[int, ...]]) -> int:
    return len([t for t in get_triangle(side_lengths) if validate(t)])


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        values = [tuple(int(v) for v in r.split()) for r in fp.readlines()]
    return solve_part_1(values), solve_part_2(values)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
