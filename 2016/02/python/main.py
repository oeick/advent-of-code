def find_start(keyboard: list[str], key: str) -> (int, int):
    for n_row, row in enumerate(keyboard):
        if (n_col := row.find(key)) > -1:
            return n_row, n_col
    raise RuntimeError(f"Could not find key '{key}'.")


def solve(keyboard: list[str], instructions: list[str]) -> str:
    n_row, n_col = find_start(keyboard, "5")
    bathroom_code = ""
    for instruction in instructions:
        for step in instruction:
            if step == 'U':
                if n_row > 0 and keyboard[n_row - 1][n_col] != '-':
                    n_row -= 1
            elif step == 'D':
                if n_row < len(keyboard) - 1 \
                        and keyboard[n_row + 1][n_col] != '-':
                    n_row += 1
            elif step == 'L':
                if n_col > 0 and keyboard[n_row][n_col - 1] != '-':
                    n_col -= 1
            elif step == 'R':
                if n_col < len(keyboard[n_row]) - 1 \
                        and keyboard[n_row][n_col + 1] != '-':
                    n_col += 1
        bathroom_code += keyboard[n_row][n_col]
    return bathroom_code


def main(filename: str) -> (str, str):
    with open(filename, 'r') as fp:
        instructions = fp.read().splitlines()
    return (
        solve(
            keyboard=[
                "123",
                "456",
                "789",
            ],
            instructions=instructions),
        solve(
            keyboard=[
                "--1--",
                "-234-",
                "56789",
                "-ABC-",
                "--D--",
            ],
            instructions=instructions),
    )


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
