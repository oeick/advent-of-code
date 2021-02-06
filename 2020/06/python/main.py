def solve(lines: list[str]) -> (int, int):
    count1, count2 = 0, 0
    group = []
    for line in lines + ['']:
        if line:
            group.append(line)
        elif len(group) > 0:
            count1 += len(set(''.join(group)))
            count2 += len(set.intersection(*[set(line) for line in group]))
            group = []
    return count1, count2


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = [line.strip() for line in fp.readlines()]
    return solve(lines)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
