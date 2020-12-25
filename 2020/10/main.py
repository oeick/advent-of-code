from itertools import groupby

with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file]

jolts = sorted([int(line) for line in lines])
jolts = [0] + jolts + [jolts[-1] + 3]

counter1, counter3 = 0, 0
for i, jolt in enumerate(jolts[:-1]):
    if jolt == jolts[i+1] - 1:
        counter1 += 1
    elif jolt == jolts[i+1] - 3:
        counter3 += 1

print(counter1 * counter3)

diffs = [jolts[i+1] - j for i, j in enumerate(jolts[:-1])]


def get_valids(number_of_ones):
    n = number_of_ones - 1
    candidates = ['{:0>{}}'.format('{:b}'.format(b), n) for b in range(2**n)]
    valid = [c + '1' for c in candidates if '000' not in c]
    return valid


product = 1
for x, group in groupby(diffs):
    if x == 1:
        n = len(list(group))
        valids = get_valids(n)
        product *= len(valids)

print(product)
