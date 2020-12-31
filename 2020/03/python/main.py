with open('../input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]

prod = 1
for slope in [1, 3, 5, 7]:
    trees = 0
    col = 0
    for row in lines:
        if row[col] == '#':
            trees += 1
        col += slope
        col = col % len(row)
    prod *= trees
    if slope == 3:
        print(trees)

trees = 0
col = 0
for i_row in range(0, len(lines), 2):
    if lines[i_row][col] == '#':
        trees += 1
    col += 1
    col = col % len(lines[0])

prod *= trees
print(prod)
