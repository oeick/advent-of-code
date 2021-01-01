with open('../input.txt', 'r') as input_file:
    instructions = input_file.read()

print(instructions.count('(') - instructions.count(')'))

floor = 0
for n, c in enumerate(instructions):
    floor += 1 if c == '(' else -1
    if floor == -1:
        print(n + 1)
        break
