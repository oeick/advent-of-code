puzzle_input = '123487596'


def format_result(cups: list[int]) -> str:
    index_of_cup1: int = cups.index(1)
    result: list[int] = cups[index_of_cup1+1:] + cups[:index_of_cup1]
    return ''.join([str(d) for d in result])


def solve(cups_str: str, rounds: int):
    cups: list[int] = [int(d) for d in cups_str]
    for _ in range(rounds):
        removed = cups[1:4]
        cups = [cups[0]] + cups[4:]
        destination = cups[0] - 1
        while destination not in cups:
            destination -= 1
            if destination < 1:
                destination = 9
        index_of_dest = cups.index(destination)
        cups = cups[:index_of_dest+1] + removed + cups[index_of_dest+1:]
        cups = cups[1:] + [cups[0]]
    return format_result(cups)


print(solve(puzzle_input, 100))
