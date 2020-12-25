with open('input.txt', 'r') as fp:
    lines = [line.strip() for line in fp.readlines()]

tokens = [line.split() for line in lines]
original_instructions = [(t[0], int(t[1])) for t in tokens]


def execute(instructions):
    i = 0
    history = []
    acc = 0
    while i not in history and i < len(instructions):
        op, arg = instructions[i]
        history.append(i)
        if op == 'jmp':
            i += arg
        else:
            i += 1
            if op == 'acc':
                acc += arg
    return acc, i in history


print(execute(original_instructions)[0])

for j, (op, arg) in enumerate(original_instructions):
    if op == 'acc':
        continue
    instructions = list(original_instructions)
    instructions[j] = ({'nop': 'jmp',
                        'jmp': 'nop'}[op],
                       arg)
    acc, infinite = execute(instructions)
    if not infinite:
        print(acc)
        break
