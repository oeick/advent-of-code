import re

with open('../input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]

pattern = re.compile(r'(\d+)-(\d+) (\w+): (.+)')

counter1, counter2 = 0, 0
for line in lines:
    matches = pattern.match(line)
    low, high = [int(d) for d in matches.groups()[:2]]
    char, code = matches.groups()[2:]
    if low <= code.count(char) <= high:
        counter1 += 1
    if (code[low - 1] == char) != (code[high - 1] == char):
        counter2 += 1

print(counter1)
print(counter2)
