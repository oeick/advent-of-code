from collections import Counter


def solve(messages: list[str]) -> (str, str):
    columns = [''.join([s[i] for s in messages])
               for i in range(len(messages[0]))]
    sol_part_1 = ''.join([Counter(c).most_common(1)[0][0] for c in columns])
    sol_part_2 = ''.join([sorted(list(Counter(c).items()),
                                 key=lambda x: x[1])[0][0] for c in columns])
    return sol_part_1, sol_part_2


def main(filename: str) -> (str, str):
    with open(filename, 'r') as fp:
        messages = fp.read().splitlines()
    return solve(messages)


if __name__ == '__main__':
    solution1, solution2 = main('../input.txt')
    print(solution1)
    print(solution2)
