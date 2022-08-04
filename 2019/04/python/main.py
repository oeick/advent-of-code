from typing import Iterator


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        first_number, second_number, *_ = fp.read().split('-')
    given_range = range(int(first_number), int(second_number))
    return solve(str(pw) for pw in given_range)


def solve(passwords: Iterator[str]) -> (int, int):
    pws = [pw for pw in passwords
           if all(pw[i] >= pw[i - 1] for i in range(1, 6))]
    return (sum(any(pw.count(d) - 1 for d in pw) for pw in pws),
            sum(any(pw.count(d) == 2 for d in pw) for pw in pws))


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
