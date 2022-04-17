import re

from balancer import Balancer
from program import Program

INPUT_PATTERN = re.compile(r'^(.+) \((\d+)\)( -> (.*))?$')


def prepare_program_from_line(line: str) -> (str, Program):
    name, weight, _, subs = re.search(INPUT_PATTERN, line).groups()
    return name, Program(weight=int(weight),
                         previous=None,
                         subs=subs.split(', ') if subs else None)


def find_and_set_previous_programs(programs: dict[str, Program]):
    for progr in programs:
        progr_subs = programs[progr].subs
        if progr_subs:
            for sub_progr in progr_subs:
                programs[sub_progr].previous = progr


def create_tree(list_entries: list[str]) -> dict[str, Program]:
    programs: dict[str, Program] = {}
    for line in list_entries:
        name, progr = prepare_program_from_line(line)
        programs[name] = progr
    find_and_set_previous_programs(programs)
    return programs


def find_root(programs: dict[str, Program]) -> str:
    progr = list(programs.keys())[0]
    while programs[progr].previous:
        progr = programs[progr].previous
    return progr


def calc_total_weight(program: str, programs: dict[str, Program]) -> int:
    weight = programs[program].weight
    subs = programs[program].subs
    if subs:
        weight += sum([calc_total_weight(p, programs) for p in subs])
    return weight


def solve_part_1(programs: dict[str, Program]) -> str:
    return find_root(programs)


def solve_part_2(programs: dict[str, Program]) -> int:
    return Balancer(programs).balance_weight()


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        programs = create_tree(fp.read().splitlines())
    return solve_part_1(programs), solve_part_2(programs)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
