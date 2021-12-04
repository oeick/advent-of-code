from collections import Counter


def solve_part_1(lines: list[str]) -> int:
    columns = [''.join(r[i] for r in lines) for i in range(len(lines[0]))]
    counts = [Counter(col).most_common() for col in columns]
    most = ''.join([c[0][0] for c in counts])
    least = ''.join([c[-1][0] for c in counts])
    return int(most, 2) * int(least, 2)


def find_common_value(
        numbers: list[str], most: bool, bit_position: int) -> str:
    column = ''.join([n[bit_position] for n in sorted(
        numbers, key=lambda c: c[bit_position], reverse=True)])
    return Counter(column).most_common()[-(not most)][0]


def get_rating(lines: list[str], oxygen: bool) -> str:
    remaining = list(lines)
    col = 0
    while len(remaining) > 1:
        criteria = find_common_value(remaining, oxygen, col)
        remaining = [r for r in remaining if r[col] == criteria]
        col += 1
    return remaining[0]


def solve_part_2(lines: list[str]) -> int:
    rating_oxy = get_rating(lines, True)
    rating_co2 = get_rating(lines, False)
    return int(rating_oxy, 2) * int(rating_co2, 2)


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    return solve_part_1(lines), solve_part_2(lines)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
