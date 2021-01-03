import re


def solve(lines: list[str]) -> (int, int):
    pattern = re.compile(r'(\d+)-(\d+) (\w+): (.+)')

    counter1, counter2 = 0, 0
    for line in lines:
        matches = pattern.match(line)
        low, high = [int(d) for d in matches.groups()[:2]]
        char, code = matches.groups()[2:]
        if low <= code.count(char) <= high:
            counter1 += 1
        if (code[low - 1] == char) != (code[high - 1] == char):
            counter2 += 1
    return counter1, counter2


def main(filename: str) -> (str, str):
    with open(filename, 'r') as input_file:
        lines = input_file.read().splitlines()
    counters = solve(lines)
    return (str(counters[0]),
            str(counters[1]))


if __name__ == '__main__':
    solutions = main('../input.txt')
    print(solutions[0])
    print(solutions[1])
