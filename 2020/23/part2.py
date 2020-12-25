puzzle_input = '123487596'

MAX_CUP = 1_000_000


def solve(cups_str, rounds):
    cup_list = list([int(d) for d in cups_str])
    cup_list.extend(range(10, MAX_CUP + 1))
    key_value_pairs = zip(
        cup_list,
        cup_list[1:] + [cup_list[0]])
    circle = dict(key_value_pairs)

    current = cup_list[0]

    for i in range(rounds):
        dest = current - 1
        pick1 = circle[current]
        pick2 = circle[pick1]
        pick3 = circle[pick2]
        while dest in [pick1, pick2, pick3] or dest < 1:
            dest -= 1
            if dest < 1:
                dest = MAX_CUP
        circle[current] = circle[pick3]
        current = circle[pick3]
        circle[pick3] = circle[dest]
        circle[dest] = pick1

    result1 = circle[1]
    result2 = circle[result1]
    return result1 * result2


print(solve(puzzle_input, 10_000_000))
