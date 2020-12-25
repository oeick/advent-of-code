with open('input.txt', 'r') as fp:
    lines = [line.strip() for line in fp.readlines()]

ids = []
for line in lines:
    row = 0
    for i, c in enumerate(line[:7]):
        half_rel = 2 ** (7 - i)
        if c == 'B':
            half_rel = int(half_rel/2)
        else:
            half_rel = 0
        row += half_rel

    col = 0
    for i, c in enumerate(line[7:]):
        half_rel = 2 ** (3 - i)
        if c == 'R':
            half_rel = int(half_rel/2)
        else:
            half_rel = 0
        col += half_rel
    ids.append(row*8 + col)

print(max(ids))

srt = sorted(ids)
for i in range(len(ids)-1):
    if srt[i] != srt[i+1]-1:
        print(srt[i] + 1)
