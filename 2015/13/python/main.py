import re
from itertools import permutations

PATTERN = re.compile(
    r'(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).')

HAPPY_TYPE = dict[str, dict[str, int]]


def parse_happiness_units(lines: list[str]) -> HAPPY_TYPE:
    result: dict[str, dict[str, int]] = {}
    for line in lines:
        first, gain, units, second = PATTERN.match(line).groups()
        if first not in result:
            result[first] = {}
        result[first][second] = int(units) if gain == 'gain' else -int(units)
    return result


def calc_happiness(arrangement: tuple[str, ...], units: HAPPY_TYPE) -> int:
    left_seat_happiness = sum(
        [units[a][arrangement[i - 1]]
         for i, a in enumerate(arrangement)]
    )
    right_seat_happiness = sum(
        [units[a][arrangement[i + 1]]
         for i, a in enumerate(arrangement[:-1])],
        units[arrangement[-1]][arrangement[0]]
    )
    return left_seat_happiness + right_seat_happiness


def append_yourself(units: HAPPY_TYPE) -> HAPPY_TYPE:
    attendees = set(units.keys())
    new_units = {a: units[a] | {'Yourself': 0} for a in attendees}
    new_units['Yourself'] = {attendee: 0 for attendee in attendees}
    return new_units


def solve_part_1(lines: list[str]) -> int:
    return solve(parse_happiness_units(lines))


def solve_part_2(lines: list[str]) -> int:
    return solve(append_yourself(parse_happiness_units(lines)))


def solve(happiness_units: HAPPY_TYPE) -> int:
    attendees = set(happiness_units.keys())
    return max([calc_happiness(arrangement, happiness_units)
                for arrangement in permutations(attendees)])


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    return solve_part_1(lines), solve_part_2(lines)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
