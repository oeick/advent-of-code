import hashlib


def solve_part1(secret_key: str) -> int:
    return find_lowest_number(
        secret_key,
        lambda b: b[0] == 0 and b[1] == 0 and b[2] < 16)


def solve_part2(secret_key: str) -> int:
    return find_lowest_number(
        secret_key,
        lambda b: b[0] == 0 and b[1] == 0 and b[2] == 0)


def find_lowest_number(secret_key: str, condition: callable) -> int:
    n = 1
    while True:
        m = hashlib.md5()
        m.update((secret_key + str(n)).encode('ascii'))
        b = m.digest()
        if condition(b):
            break
        n += 1
    return n


def main(filename: str) -> (int, int):
    with open(filename, 'r') as input_file:
        secret_key = input_file.read()
    return (solve_part1(secret_key),
            solve_part2(secret_key))


if __name__ == '__main__':
    solutions = main('../input.txt')
    print(solutions[0])
    print(solutions[1])
