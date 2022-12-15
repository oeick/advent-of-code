def main(filename: str) -> tuple[int, str]:
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    return solve(lines)


def solve(lines: list[str]) -> tuple[int, str]:
    register = calc_register(lines)
    signal_strength = [register[i-1] * i for i in (20, 60, 100, 140, 180, 220)]
    return sum(signal_strength), draw_image(register)


def draw_image(register: list[int]) -> str:
    return '\n'.join(generate_rows(register))


def generate_rows(register: list[int]) -> list[str]:
    rows: list[str] = []
    row = ''
    for i in range(len(register)):
        row += '#' if register[i] - 2 < len(row) < register[i] + 2 else '.'
        if len(row) == 40:
            rows.append(row)
            row = ''
    return rows


def calc_register(lines: list[str]) -> list[int]:
    register, value = [], 1
    for line in lines:
        if line == 'noop':
            register += cycle(1, value)
        else:
            register += cycle(2, value)
            value += int(line.split()[-1])
    register.append(value)
    return register


def cycle(value: int, register: int) -> list[int]:
    return [register for _ in range(value)]


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
