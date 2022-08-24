from computer import Computer


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        integers = {n: int(d) for n, d in enumerate(fp.read().split(','))}
    return solve(integers, 1), solve(integers, 2)


def solve(program: dict[int, int], inp: int) -> int:
    cmp = Computer(program, [inp, ])
    result = []
    while (out := cmp.run()) is not None:
        result.append(out)
    if len(result) != 1:
        raise ValueError(f'error, output: {result}')
    return result[0]


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
