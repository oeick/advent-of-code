from typing import Generator


def solve(instructions: list[str]) -> (int, int):
    registers: dict[str, int] = {}
    peak: int = 0
    for target_register, condition_register, expression in parsed(instructions):
        registers = {target_register: 0, condition_register: 0} | registers
        registers[target_register] = eval(expression, registers)
        peak = max(peak, registers[target_register])
    del(registers['__builtins__'])
    return max(registers.values()), peak


def parse(instr: str) -> (str, str, str):
    target, _, _, _, cond, _ = instr.split(maxsplit=5)
    expr = instr.replace('inc', '+').replace('dec', '-') + ' else ' + target
    return target, cond, expr


def parsed(instructions: list[str]) -> Generator:
    return (parse(i) for i in instructions)


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        instructions = fp.read().splitlines()
    return solve(instructions)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
