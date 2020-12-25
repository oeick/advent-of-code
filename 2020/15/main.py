inp = '19,0,5,1,10,13'

input_spoken: list = [int(d) for d in inp.split(',')]


def solve(spoken, rounds):
    indices = {n: i for i, n in enumerate(spoken)}
    previous_i = {n: -1 for n in spoken}
    i = len(spoken)
    next_spoken = spoken[-1]
    while i < rounds:
        last_spoken = next_spoken
        if previous_i[last_spoken] == -1:
            next_spoken = 0
        else:
            next_spoken = indices[last_spoken] - previous_i[last_spoken]
        previous_i[next_spoken] = indices.get(next_spoken, -1)
        indices[next_spoken] = i
        i += 1

    return next_spoken


print(solve(input_spoken, 2020))
print(solve(input_spoken, 30000000))
