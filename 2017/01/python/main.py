def solve_part_1(captcha: str) -> int:
    shifted = captcha[1:] + captcha[0]
    return sum(int(a) for a, b in zip(captcha, shifted) if a == b)


def solve_part_2(captcha: str) -> int:
    middle = len(captcha) // 2
    half_1 = captcha[:middle]
    half_2 = captcha[middle:]
    return 2 * sum(int(a) for a, b in zip(half_1, half_2) if a == b)


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        captcha = fp.read()
    return solve_part_1(captcha), solve_part_2(captcha)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
