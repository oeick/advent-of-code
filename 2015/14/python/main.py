import re
from typing import NamedTuple

PATTERN = re.compile(r'(\w+) can fly (\d+) km/s for (\d+) seconds, '
                     r'but then must rest for (\d+) seconds.')


DURATION = 2503


class Specs(NamedTuple):
    speed: int
    fly: int
    rest: int


def parse_input_lines(lines: list[str]) -> dict[Specs]:
    parsed = {}
    for line in lines:
        reindeer, speed, fly, rest = PATTERN.match(line).groups()
        parsed[reindeer] = Specs(int(speed), int(fly), int(rest))
    return parsed


def calc_distance(duration: int, reindeer: Specs) -> int:
    periods, remaining = divmod(duration, reindeer.fly + reindeer.rest)
    return reindeer.speed * (periods * reindeer.fly +
                             min(remaining, reindeer.fly))


def solve(reindeer: dict[Specs]) -> (int, int):
    distances = [calc_distance(DURATION, r) for r in reindeer.values()]
    return max(distances), 0


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.readlines()
    return solve(parse_input_lines(lines))


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
