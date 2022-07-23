import re
from collections import defaultdict, Counter

MATCH_GUARD_BEGINS_SHIFT = re.compile(r"Guard #(\d+) begins shift")
MATCH_FALLS_ASLEEP = re.compile(r":(\d+)] falls asleep")
MATCH_WAKES_UP = re.compile(r":(\d+)] wakes up")


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = sorted(fp.read().splitlines())
    guard_sleep_minutes = get_guard_sleep_minutes(lines)
    return solve_part_1(guard_sleep_minutes), solve_part_2(guard_sleep_minutes)


def get_guard_sleep_minutes(lines: list[str]) -> dict[int, list[int]]:
    guard_sleep_minutes = defaultdict(list)
    guard_id: int = 0
    minute_sleep: int = 0
    for line in lines:
        if match_begin := re.search(MATCH_GUARD_BEGINS_SHIFT, line):
            guard_id = int(match_begin.group(1))
        elif match_asleep := re.search(MATCH_FALLS_ASLEEP, line):
            minute_sleep = int(match_asleep.group(1))
        elif match_wakeup := re.search(MATCH_WAKES_UP, line):
            minute_wake = int(match_wakeup.group(1))
            guard_sleep_minutes[guard_id] += range(minute_sleep, minute_wake)
    return guard_sleep_minutes


def solve_part_1(guard_sleep_minutes: dict[int, list[int]]) -> int:
    total_minutes = [(len(m), g) for g, m in guard_sleep_minutes.items()]
    guard = max(total_minutes)[1]
    most_common_min = Counter(guard_sleep_minutes[guard]).most_common()[0][0]
    return guard * most_common_min


def solve_part_2(guard_sleep_minutes: dict[int, list[int]]) -> int:
    most_common_minutes = [(g, Counter(m).most_common()[0][0])
                           for g, m in guard_sleep_minutes.items()]
    counts_of_same_minute = [(guard_sleep_minutes[i].count(m), i, m)
                             for i, m in most_common_minutes]
    _, guard_id, minute = max(counts_of_same_minute)
    return guard_id * minute


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
