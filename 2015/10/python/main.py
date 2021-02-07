def split_into_sublists(string: str) -> list[list[str]]:
    previous = None
    sublists = []
    for char in string:
        if char != previous:
            sublists.append([char])
        else:
            sublists[-1].append(char)
        previous = char
    return sublists


def look_and_say(input_str: str) -> str:
    sub_lists = split_into_sublists(input_str)
    return ''.join([str(len(s)) + s[0] for s in sub_lists])


def solve(input_str: str, rounds: int) -> int:
    result = input_str
    for i in range(rounds):
        result = look_and_say(result)
    return len(result)


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        line = fp.read()
    return solve(line, 40), solve(line, 50)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
