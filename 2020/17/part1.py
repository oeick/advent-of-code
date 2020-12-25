input_string = """
##.#####
#.##..#.
.##...##
###.#...
.#######
##....##
###.###.
.#.#.#.."""


def print_state(state):
    x_min = min(c[0] for c in state)
    x_max = max(c[0] for c in state)
    y_min = min(c[1] for c in state)
    y_max = max(c[1] for c in state)
    z_min = min(c[2] for c in state)
    z_max = max(c[2] for c in state)
    for z in range(z_min, z_max+1):
        for y in range(y_min, y_max+1):
            print(''.join(["#" if (x, y, z) in state else "."
                           for x in range(x_min, x_max+1)]))
        print()


def calc_neighbor_coords(x0, y0, z0):
    return ((x, y, z)
            for x in (x0-1, x0, x0+1)
            for y in (y0-1, y0, y0+1)
            for z in (z0-1, z0, z0+1)
            if x != x0 or y != y0 or z != z0)


def count_active_neighbors(x0, y0, z0, state):
    coords = calc_neighbor_coords(x0, y0, z0)
    return sum(1 for c in coords if c in state)


def generate_next_state(prev_state):
    next_state = {cube
                  for cube in prev_state
                  if 2 <= count_active_neighbors(*cube, state=prev_state) <= 3}
    inactive = {c
                for a in prev_state
                for c in calc_neighbor_coords(*a)
                if c not in prev_state}
    for cube in inactive:
        if count_active_neighbors(*cube, state=prev_state) == 3:
            next_state.add(cube)
    return next_state


current_state = {(x, y, 0)
                 for y, r in enumerate(input_string.split())
                 for x, s in enumerate(r)
                 if s == '#'}

for cycle in range(6):
    current_state = generate_next_state(current_state)

print(len(current_state))
