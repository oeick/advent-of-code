import re
from typing import NamedTuple

PATTERN = re.compile(r'(\w+) can fly (\d+) km/s for (\d+) seconds, '
                     r'but then must rest for (\d+) seconds.')


class Specs(NamedTuple):
    speed: int
    fly: int
    rest: int


def parse_input_lines(lines: list[str]) -> dict[str, Specs]:
    parsed = {}
    for line in lines:
        reindeer, speed, fly, rest = PATTERN.match(line).groups()
        parsed[reindeer] = Specs(int(speed), int(fly), int(rest))
    return parsed


def calc_distance(duration: int, reindeer: Specs) -> int:
    periods, remaining = divmod(duration, reindeer.fly + reindeer.rest)
    return reindeer.speed * (periods * reindeer.fly +
                             min(remaining, reindeer.fly))


def calc_points(duration: int, reindeer: dict[str, Specs]) -> dict[str, int]:
    points = dict(zip(reindeer.keys(), [0 for _ in reindeer]))
    for dur in range(1, duration + 1):
        distances = {nick: calc_distance(dur, specs)
                     for nick, specs in reindeer.items()}
        best = max(distances, key=lambda k: distances[k])
        for r in reindeer:
            if distances[r] == distances[best]:
                points[r] += 1
    return points


def solve(duration: int, reindeer: dict[str, Specs]) -> (int, int):
    distances = [calc_distance(duration, r) for r in reindeer.values()]
    points = calc_points(duration, reindeer).values()
    return max(distances), max(points)


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.readlines()
    return solve(duration=2503,
                 reindeer=parse_input_lines(lines))


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
