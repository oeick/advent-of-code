import re
from collections import namedtuple

PATTERN = re.compile(r"([a-z0-9]*)\s?([A-Z]*)\s?([a-z0-9]*) -> (.*)")

Instruction = namedtuple('Instruction',
                         ['param1', 'operation', 'param2', 'target'])


def solve(instructions: list[Instruction]) -> dict[str, int]:
    instructions = [Instruction(**i._asdict()) for i in instructions]
    wires: dict[str, int] = {}
    j = 0
    while len(instructions) > 0:
        param1, op, param2, target = instructions[j]
        param1 = wires.get(param1, int(param1) if param1.isnumeric() else None)
        param2 = wires.get(param2, int(param2) if param2.isnumeric() else None)
        if op == '' and param1 is not None:
            wires[target] = param1
            instructions.pop(j)
        if op == 'NOT' and param2 is not None:
            wires[target] = ~param2 & 0xFFFF
            instructions.pop(j)
        if op == 'AND' and param1 is not None and param2 is not None:
            wires[target] = param1 & param2
            instructions.pop(j)
        if op == 'OR' and param1 is not None and param2 is not None:
            wires[target] = param1 | param2
            instructions.pop(j)
        if op == 'LSHIFT' and param1 is not None:
            wires[target] = param1 << param2
            instructions.pop(j)
        if op == 'RSHIFT' and param1 is not None:
            wires[target] = param1 >> param2
            instructions.pop(j)
        j += 1
        if j >= len(instructions):
            j = 0
    return wires


def parse_instructions(lines: list[str]) -> list[Instruction]:
    instructions = []
    for line in lines:
        matches = re.match(PATTERN, line)
        instructions.append(Instruction(*matches.groups()))
    return instructions


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    instructions = parse_instructions(lines)
    wire_a_part_1 = solve(instructions)['a']
    instructions = [Instruction(str(wire_a_part_1), '', '', 'b')
                    if i.target == 'b' else i
                    for i in instructions]
    wire_a_part_2 = solve(instructions)['a']
    return wire_a_part_1, wire_a_part_2


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
