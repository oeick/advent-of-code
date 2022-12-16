INSTRUCTIONS = list[tuple[int, int, int]]


def main(filename: str) -> tuple[str, str]:
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    moves = [line.split(' ') for line in lines if line.startswith('move')]
    instr = [(int(i[1]), int(i[3]), int(i[5])) for i in moves]
    crates = ['-'] + parse_crates(lines)
    return solve1(crates, instr), solve2(crates, instr)


def parse_crates(lines: list[str]) -> list[str]:
    crates: dict[int, str] = {}
    for line in lines:
        if line.startswith(' 1'):
            break
        for i in range(0, len(line), 4):
            n = i // 4
            c = line[i + 1:i + 2]
            if c != ' ':
                crates[n] = c + crates[n] if n in crates else c
    return [crates[n] for n in range(1 + max(crates.keys()))]


def solve1(initial_crates: list[str], instr: INSTRUCTIONS) -> str:
    crates = initial_crates.copy()
    for n, f, t in instr:
        for _ in range(n):
            c = crates[f][-1]
            crates[f] = crates[f][:-1]
            crates[t] = crates[t] + c
    return ''.join(c[-1] for c in crates[1:])


def solve2(initial_crates: list[str], instr: INSTRUCTIONS) -> str:
    crates = initial_crates.copy()
    for n, f, t in instr:
        c = crates[f][-n:]
        crates[f] = crates[f][:-n]
        crates[t] = crates[t] + c
    return ''.join(c[-1] for c in crates[1:])


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
