from itertools import count
from typing import Optional


def calc_scan_step(scan_range: int, depth: int, time: int) -> int:
    return (time + depth) % (2 * (scan_range - 1))


def get_total_severity(
        scanner: dict[int, int], delay: int = 0) -> Optional[int]:
    severities = [depth * rng
                  for depth, rng in scanner.items()
                  if calc_scan_step(rng, depth, delay) == 0]
    return sum(severities) if severities else None


def find_safe_delay(scanner: dict[int, int]) -> int:
    for time in count():
        for depth, scan_range in scanner.items():
            if calc_scan_step(scan_range, depth, time) == 0:
                break
        else:
            return time


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        tokens = [line.strip().split(':') for line in fp]
    ranges = {int(d): int(r) for d, r in tokens}
    return (
        get_total_severity(ranges),
        find_safe_delay(ranges))


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
