from collections import namedtuple

with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file]

#           (1, 0)
#             N
#             |
# (0, -1) W --+-- E (0, 1)
#             |
#             S
#           (-1, 0)

rotate = {
    (1, 0, 'L90'): (0, -1),
    (1, 0, 'L180'): (-1, 0),
    (1, 0, 'L270'): (0, 1),
    (-1, 0, 'L90'): (0, 1),
    (-1, 0, 'L180'): (1, 0),
    (-1, 0, 'L270'): (0, -1),
    (1, 0, 'R90'): (0, 1),
    (1, 0, 'R180'): (-1, 0),
    (1, 0, 'R270'): (0, -1),
    (-1, 0, 'R90'): (0, -1),
    (-1, 0, 'R180'): (1, 0),
    (-1, 0, 'R270'): (0, 1),

    (0, 1, 'L90'): (1, 0),
    (0, 1, 'L180'): (0, -1),
    (0, 1, 'L270'): (-1, 0),
    (0, -1, 'L90'): (-1, 0),
    (0, -1, 'L180'): (0, 1),
    (0, -1, 'L270'): (1, 0),
    (0, 1, 'R90'): (-1, 0),
    (0, 1, 'R180'): (0, -1),
    (0, 1, 'R270'): (1, 0),
    (0, -1, 'R90'): (1, 0),
    (0, -1, 'R180'): (0, 1),
    (0, -1, 'R270'): (-1, 0),
}

Vector = namedtuple('Position', ['x', 'y'])
pos = Vector(0, 0)
facing = Vector(0, 1)
for line in lines:
    action, value = line[0], int(line[1:])
    if action == 'F':
        pos = Vector(
            pos.x + facing.x * value,
            pos.y + facing.y * value)
    elif action == 'N':
        pos = Vector(pos.x + value, pos.y)
    elif action == 'S':
        pos = Vector(pos.x - value, pos.y)
    elif action == 'E':
        pos = Vector(pos.x, pos.y + value)
    elif action == 'W':
        pos = Vector(pos.x, pos.y - value)
    elif action in ('L', 'R'):
        facing = Vector(*rotate[(*facing, line)])

print(sum(abs(p) for p in pos))


def rotate_wp(wp, instruction):
    return {'L90': Vector(wp.y, -wp.x),
            'L180': Vector(-wp.x, -wp.y),
            'L270': Vector(-wp.y, wp.x),
            'R90': Vector(-wp.y, wp.x),
            'R180': Vector(-wp.x, -wp.y),
            'R270': Vector(wp.y, -wp.x)}[instruction]


pos = Vector(0, 0)
waypoint = Vector(1, 10)
for line in lines:
    action, value = line[0], int(line[1:])
    if action == 'F':
        pos = Vector(
            pos.x + waypoint.x * value,
            pos.y + waypoint.y * value)
    elif action == 'N':
        waypoint = Vector(waypoint.x + value, waypoint.y)
    elif action == 'S':
        waypoint = Vector(waypoint.x - value, waypoint.y)
    elif action == 'E':
        waypoint = Vector(waypoint.x, waypoint.y + value)
    elif action == 'W':
        waypoint = Vector(waypoint.x, waypoint.y - value)
    elif action in ('L', 'R'):
        waypoint = rotate_wp(waypoint, line)

print(sum(abs(p) for p in pos))
