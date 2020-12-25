with open('input.txt', 'r') as fp:
    lines = [line.strip() for line in fp.readlines()]

grid = [[col for col in row] for row in lines]


def num_of_next_occ(grid, i_row, i_col):
    num = 0
    for r in [i_row-1, i_row, i_row+1]:
        if r < 0 or r >= len(grid):
            continue
        for c in [i_col-1, i_col, i_col+1]:
            if c < 0 or c >= len(grid[r]):
                continue
            if grid[r][c] == '#' and not (r == i_row and c == i_col):
                num += 1
    return num


def do_round(grid0, occ_checker, max_occ):
    grid1 = [list(r) for r in grid0]
    for ir, row in enumerate(grid0):
        for ic, pos in enumerate(row):
            occ = occ_checker(grid0, ir, ic)
            if pos == 'L' and occ == 0:
                grid1[ir][ic] = '#'
            if pos == '#' and occ > max_occ:
                grid1[ir][ic] = 'L'
    return grid1


def solve(input_grid, occ_checker, max_occ):
    g1 = input_grid
    changes = True
    while changes:
        g2 = do_round(g1, occ_checker, max_occ)
        if g2 == g1:
            changes = False
        else:
            g1 = g2

    num_occ_seats = 0
    for row in g1:
        for pos in row:
            if pos == '#':
                num_occ_seats += 1

    return num_occ_seats


def num_of_seen_occ(grid, i_row, i_col):
    incrementors = [(1, 0), (-1, 0),
                    (0, 1), (0, -1),
                    (1, 1), (-1, -1),
                    (1, -1), (-1, 1)]
    count = 0
    for inc in incrementors:
        r = i_row
        c = i_col
        while True:
            r += inc[0]
            c += inc[1]
            if r < 0 or r >= len(grid):
                break
            if c < 0 or c >= len(grid[r]):
                break
            if grid[r][c] == 'L':
                break
            elif grid[r][c] == '#':
                count += 1
                break
    return count


print(solve(grid, num_of_next_occ, 3))
print(solve(grid, num_of_seen_occ, 4))
