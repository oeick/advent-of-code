import re


def calc_index(row: int, column: int) -> int:
    return column + (row + column - 1) * (row + column - 2) // 2


def calc_code(index: int) -> int:
    v = 20151125
    for i in range(1, index):
        v = v * 252533 % 33554393
    return v


def solve(row: int, column: int) -> int:
    index = calc_index(row, column)
    code = calc_code(index)
    return code


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        line = fp.read()
    match = re.match(r'.*row (\d+), column (\d+).*', line).groups()
    row, column = [int(v) for v in match]
    return solve(row, column)


if __name__ == '__main__':
    solution = main('../input.txt')
    print(solution)
