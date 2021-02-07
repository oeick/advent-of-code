def increase_password(password: str) -> str:
    last_char = password[-1]
    new_char = chr(ord(last_char) + 1)
    if new_char <= 'z':
        return password[:-1] + new_char
    else:
        return increase_password(password[:-1]) + 'a'


def two_pairs(password: str) -> bool:
    m = [i for i in range(len(password) - 1)
         if password[i] == password[i + 1]]
    if not m:
        return False
    return m[0]+1 < m[-1]


def is_valid(password: str) -> bool:
    if any(c in password for c in 'iol'):
        return False
    if not two_pairs(password):
        return False
    if not any(ord(password[i]) == ord(password[i + 1]) - 1
               and ord(password[i + 1]) == ord(password[i + 2]) - 1
               for i in range(len(password) - 2)):
        return False
    return True


def solve(initial_password: str) -> str:
    password = increase_password(initial_password)
    while not is_valid(password):
        password = increase_password(password)
    return password


def main(filename: str) -> (str, str):
    with open(filename, 'r') as fp:
        line = fp.read()
    password_1 = solve(line)
    password_2 = solve(password_1)
    return password_1, password_2


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
