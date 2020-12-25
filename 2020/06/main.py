with open('input.txt', 'r') as fp:
    lines = [line.strip() for line in fp.readlines()] + ['']


count1, count2 = 0, 0
group = []
for line in lines:
    if line:
        group.append(line)
    else:
        count1 += len(set(''.join(group)))
        count2 += len(set.intersection(*[set(line) for line in group]))
        group = []

print(count1)
print(count2)
