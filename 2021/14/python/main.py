from collections import Counter
from functools import cache

RULES = dict[tuple[str, str], str]


class Solver:
    rules: RULES

    def __init__(self, rules: RULES):
        self.rules = rules

    def solve(self, template: str, steps: int) -> int:
        counts = self.count_elements(template, steps)
        most = counts.most_common()
        return most[0][1] - most[-1][1]

    def count_elements(self, template: str, steps: int) -> Counter:
        pairs = [(template[i], template[i + 1])
                 for i in range(len(template) - 1)]
        result = Counter()
        for pair in pairs:
            result += self.apply(pair[0], pair[1], steps)
        result[template[-1]] += 1
        return result

    @cache
    def apply(self, left: str, right: str, steps: int) -> Counter:
        if steps == 0:
            return Counter((left,))
        c = self.rules[(left, right)]
        return self.apply(left, c, steps - 1) + self.apply(c, right, steps - 1)


def parse_rules(lines: list[str]) -> RULES:
    rule_lines = [line.split(' -> ') for line in lines]
    return {(a[0], a[1]): b for a, b in rule_lines}


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    template = lines[0]
    rules = parse_rules(lines[2:])
    solution1 = Solver(rules).solve(template, 10)
    solution2 = Solver(rules).solve(template, 40)
    return solution1, solution2


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
