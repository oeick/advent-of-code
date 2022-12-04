def main(filename: str) -> tuple[int, int]:
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    return solve_part_1(lines), solve_part_2(lines)


def solve_part_1(lines: list[str]) -> int:
    return sum(calc_round_score(r) for r in lines)


def solve_part_2(lines: list[str]) -> int:
    rounds = [line.split(' ') for line in lines]
    return sum(calc_round_score(opp + ' ' + choose_for(opp, need))
               for opp, need in rounds)


def choose_for(opp: str, need: str) -> str:
    return {('A', 'X'): 'Z',
            ('A', 'Y'): 'X',
            ('A', 'Z'): 'Y',
            ('B', 'X'): 'X',
            ('B', 'Y'): 'Y',
            ('B', 'Z'): 'Z',
            ('C', 'X'): 'Y',
            ('C', 'Y'): 'Z',
            ('C', 'Z'): 'X'
            }[(opp, need)]


def calc_round_score(line: str) -> int:
    return {'A X': 3,
            'A Y': 6,
            'A Z': 0,
            'B X': 0,
            'B Y': 3,
            'B Z': 6,
            'C X': 6,
            'C Y': 0,
            'C Z': 3
            }[line] + ord(line[2]) - ord('X') + 1


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
