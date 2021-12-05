from typing import Iterable, Sequence

BINGOBOARD = Iterable[list[int]]
BINGOBOARDS = Sequence[BINGOBOARD]
BINGOSIZE = 5
SCORES = list[tuple[int, int]]


def mark_number(board: BINGOBOARD, number: int):
    for row in board:
        if number in row:
            row[row.index(number)] = -1
            break


def has_board_won(board: BINGOBOARD) -> bool:
    return \
        any(all(n == -1 for n in row) for row in board) or \
        any(all(row[col] == -1 for row in board) for col in range(BINGOSIZE))


def sum_unmarked(board: BINGOBOARD) -> int:
    return sum(sum(n for n in row if n >= 0) for row in board)


def parse_boards(lines: list[str]) -> Sequence[BINGOBOARD]:
    boards = []
    for i in range(len(lines) // (BINGOSIZE + 1)):
        boards.append([[int(n) for n in lines[i*(BINGOSIZE+1)+j+1].split()]
                       for j in range(BINGOSIZE)])
    return boards


def find_all_winners(
        boards: BINGOBOARDS, number: int, scores: SCORES, i_b: int) -> bool:
    if i_b not in [i for i, _ in scores]:
        mark_number(boards[i_b], number)
        if has_board_won(boards[i_b]):
            scores.append((i_b, number * sum_unmarked(boards[i_b])))
            if len(scores) == len(boards):
                return True
    return False


def solve(numbers: Iterable[int], boards: Sequence[BINGOBOARD]) -> (int, int):
    scores: list[tuple[int, int]] = []
    for number in numbers:
        for i_b in range(len(boards)):
            if find_all_winners(boards, number, scores, i_b):
                return scores[0][1], scores[-1][1]


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    numbers = [int(t) for t in lines[0].split(',')]
    boards = parse_boards(lines[1:])
    return solve(numbers, boards)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
