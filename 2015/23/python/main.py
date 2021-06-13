def process_instructions(
        instructions: list[str],
        start_values: dict[str, int]) -> dict[str, int]:
    registers = dict(start_values)
    pointer = 0
    while pointer < len(instructions):
        operator, argument = instructions[pointer].split(maxsplit=1)
        if operator == "hlf":
            registers[argument] //= 2
        elif operator == "tpl":
            registers[argument] *= 3
        elif operator == "inc":
            registers[argument] += 1
        elif operator == "jmp":
            pointer += int(argument) - 1
        elif operator == "jie":
            arg1, arg2 = argument.split(", ")
            if registers[arg1] % 2 == 0:
                pointer += int(arg2) - 1
        elif operator == "jio":
            arg1, arg2 = argument.split(", ")
            if registers[arg1] == 1:
                pointer += int(arg2) - 1
        pointer += 1
    return registers


def solve(lines: list[str]) -> (int, int):
    return (process_instructions(lines, {"a": 0, "b": 0})["b"],
            process_instructions(lines, {"a": 1, "b": 0})["b"])


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    return solve(lines)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
