from typing import NamedTuple, Callable, Optional


class Parameter(NamedTuple):
    value: int
    mode: int

    def get_position(self, computer) -> int:
        if self.mode == 0:
            return self.value
        elif self.mode == 2:
            return self.value + computer.rel_base
        else:
            raise ValueError(
                f'unsupported mode for getting position: {self.mode}')

    def read(self, computer) -> int:
        if self.mode == 0:
            return computer.program.get(self.value, 0)
        elif self.mode == 1:
            return self.value
        elif self.mode == 2:
            return computer.program.get(computer.rel_base + self.value, 0)
        else:
            raise ValueError(
                f'unsupported mode for reading value: {self.mode}')


class Operator(NamedTuple):
    function: Callable
    parameter_count: int


def add(computer, params: list[Parameter]):
    target = params[2].get_position(computer)
    summand1 = params[0].read(computer)
    summand2 = params[1].read(computer)
    computer.program[target] = summand1 + summand2
    computer.instr_pointer += 4


def multiply(computer, params: list[Parameter]):
    target = params[2].get_position(computer)
    factor1 = params[0].read(computer)
    factor2 = params[1].read(computer)
    computer.program[target] = factor1 * factor2
    computer.instr_pointer += 4


def save(computer, params: list[Parameter]):
    target = params[0].get_position(computer)
    if len(computer.inp) > 0:
        computer.program[target] = computer.inp.pop(0)
    else:
        computer.program[target] = 0
    computer.instr_pointer += 2


def output(computer, params: list[Parameter]):
    computer.out = params[0].read(computer)
    computer.instr_pointer += 2


def jump_if_true(computer, params: list[Parameter]):
    if params[0].read(computer) > 0:
        computer.instr_pointer = params[1].read(computer)
    else:
        computer.instr_pointer += 3


def jump_if_false(computer, params: list[Parameter]):
    if params[0].read(computer) == 0:
        computer.instr_pointer = params[1].read(computer)
    else:
        computer.instr_pointer += 3


def less_than(computer, params: list[Parameter]):
    target = params[2].get_position(computer)
    left = params[0].read(computer)
    right = params[1].read(computer)
    computer.program[target] = int(left < right)
    computer.instr_pointer += 4


def equals(computer, params: list[Parameter]):
    target = params[2].get_position(computer)
    left = params[0].read(computer)
    right = params[1].read(computer)
    computer.program[target] = int(left == right)
    computer.instr_pointer += 4


def adjust_rel_base(computer, params: list[Parameter]):
    computer.rel_base += params[0].read(computer)
    computer.instr_pointer += 2


class Computer:
    program: dict[int, int]
    instr_pointer: int
    inp: list[int]
    out: int
    rel_base: int
    operations: dict[int, Operator] = {1: Operator(add, 3),
                                       2: Operator(multiply, 3),
                                       3: Operator(save, 1),
                                       4: Operator(output, 1),
                                       5: Operator(jump_if_true, 2),
                                       6: Operator(jump_if_false, 2),
                                       7: Operator(less_than, 3),
                                       8: Operator(equals, 3),
                                       9: Operator(adjust_rel_base, 1)}

    def __init__(self, program: dict[int, int], inp: list[int]):
        self.program = dict(program)
        self.instr_pointer = 0
        self.inp = inp
        self.out = 0
        self.rel_base = 0

    def run(self) -> Optional[int]:
        while self.program[self.instr_pointer] != 99:
            result = self.operate()
            if result is not None:
                return result
        else:
            return None

    def operate(self) -> Optional[int]:
        instruction, modes = self.parse_instruction()
        params = []
        for i in range(instruction.parameter_count):
            value = self.program[self.instr_pointer + 1 + i]
            mode = 0 if i >= len(modes) else modes[i]
            params.append(Parameter(value, mode))
        instruction.function(self, params)
        return self.out if instruction.function == output else None

    def parse_instruction(self) -> (Operator, list[int]):
        instruction = self.operations[self.program[self.instr_pointer] % 100]
        modes_str = str(self.program[self.instr_pointer])[:-2]
        modes = [int(m) for m in modes_str[::-1]]
        return instruction, modes
