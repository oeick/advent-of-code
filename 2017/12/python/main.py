import re

LINE_PATTERN = re.compile(r'(\d+)\s<->\s(.*)')


def find_group_members(pipes: list[set[int]], start_member=0) -> set[int]:
    included = {start_member, }
    included_prev = set()
    while included != included_prev:
        included_prev = included.copy()
        for i, pipe in enumerate(pipes):
            if i in included or pipe & included:
                included |= pipe | {i}
    return included


def find_groups(pipes: list[set[int]]) -> list[set[int]]:
    groups = []
    still_searching = True
    group_id = 0
    while still_searching:
        groups.append(find_group_members(pipes, group_id))
        while group_id in set.union(*groups):
            group_id += 1
            if group_id == len(pipes):
                still_searching = False
                break
    return groups


def solve_part_1(pipes: list[set[int]]) -> (int, int):
    return len(find_group_members(pipes))


def solve_part_2(pipes: list[set[int]]) -> int:
    return len(find_groups(pipes))


def parse_line(line: str) -> set[int]:
    return {int(m) for m in re.match(LINE_PATTERN, line)[2].split(', ')}


def main(filename: str) -> (int, int):
    with open(filename) as fp:
        pipes = [parse_line(line) for line in fp]
    return solve_part_1(pipes), solve_part_2(pipes)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
