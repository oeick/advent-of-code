from typing import NamedTuple, Callable, Optional


class Operator(NamedTuple):
    function: Callable
    parameter_count: int


def add(computer, params: list[int]):
    target = computer.program[computer.instr_pointer + 3]
    computer.program[target] = params[0] + params[1]
    computer.instr_pointer += 4


def multiply(computer, params: list[int]):
    target = computer.program[computer.instr_pointer + 3]
    computer.program[target] = params[0] * params[1]
    computer.instr_pointer += 4


def save(computer, _):
    target = computer.program[computer.instr_pointer + 1]
    if len(computer.inp) > 0:
        computer.program[target] = computer.inp.pop(0)
    else:
        computer.program[target] = 0
    computer.instr_pointer += 2


def output(computer, params: list[int]):
    computer.out = params[0]
    computer.instr_pointer += 2


def jump_if_true(computer, params: list[int]):
    if params[0] > 0:
        computer.instr_pointer = params[1]
    else:
        computer.instr_pointer += 3


def jump_if_false(computer, params: list[int]):
    if params[0] == 0:
        computer.instr_pointer = params[1]
    else:
        computer.instr_pointer += 3


def less_than(computer, params: list[int]):
    target = computer.program[computer.instr_pointer + 3]
    computer.program[target] = int(params[0] < params[1])
    computer.instr_pointer += 4


def equals(computer, params: list[int]):
    target = computer.program[computer.instr_pointer + 3]
    computer.program[target] = int(params[0] == params[1])
    computer.instr_pointer += 4


class Computer:
    program: list[int]
    instr_pointer: int
    inp: list[int]
    out: int
    operations: dict[int, Operator] = {1: Operator(add, 2),
                                       2: Operator(multiply, 2),
                                       3: Operator(save, 0),
                                       4: Operator(output, 1),
                                       5: Operator(jump_if_true, 2),
                                       6: Operator(jump_if_false, 2),
                                       7: Operator(less_than, 2),
                                       8: Operator(equals, 2)}

    def __init__(self, program: list[int], inp: list[int]):
        self.program = list(program)
        self.instr_pointer = 0
        self.inp = inp
        self.out = 0

    def run(self) -> Optional[int]:
        while self.program[self.instr_pointer] != 99:
            if result := self.operate():
                return result
        else:
            return None

    def operate(self) -> Optional[int]:
        instruction, modes = self.parse_instruction()
        params_start = self.instr_pointer + 1
        params_end = params_start + instruction.parameter_count
        params = [p if i < len(modes) and modes[i] == 1 else self.program[p]
                  for i, p in enumerate(self.program[params_start:params_end])]
        instruction.function(self, params)
        return self.out if instruction.function == output else None

    def parse_instruction(self) -> (Operator, list[int]):
        instruction = self.operations[self.program[self.instr_pointer] % 100]
        modes_str = str(self.program[self.instr_pointer])[:-2]
        modes = [int(m) for m in modes_str[::-1]]
        return instruction, modes
