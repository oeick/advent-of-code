def get_row(characters: str) -> int:
    row = 0
    for i, c in enumerate(characters[:7]):
        half_rel = 2 ** (7 - i)
        if c == 'B':
            half_rel = int(half_rel/2)
        else:
            half_rel = 0
        row += half_rel
    return row


def get_column(characters: str) -> int:
    column = 0
    for i, c in enumerate(characters[7:]):
        half_rel = 2 ** (3 - i)
        if c == 'R':
            half_rel = int(half_rel / 2)
        else:
            half_rel = 0
        column += half_rel
    return column


def get_seat_ids(lines: list[str]) -> list[int]:
    ids = []
    for line in lines:
        row = get_row(line)
        col = get_column(line)
        ids.append(row*8 + col)
    return ids


def solve_part1(ids: list[int]) -> int:
    return max(ids)


def solve_part2(ids: list[int]) -> int:
    srt = sorted(ids)
    for i in range(len(ids) - 1):
        if srt[i] != srt[i + 1] - 1:
            return srt[i] + 1


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = [line.strip() for line in fp.readlines()]
    ids = get_seat_ids(lines)
    return (solve_part1(ids),
            solve_part2(ids))


if __name__ == '__main__':
    solution_1, solution_2 = main('input.txt')
    print(solution_1)
    print(solution_2)
