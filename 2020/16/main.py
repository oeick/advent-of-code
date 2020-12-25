import functools
import re

with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file]


field_range_pattern = re.compile(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)')

field_ranges = {}
your_ticket = None
nearby_tickets = []


def parse_field_ranges(line):
    match = field_range_pattern.match(line)
    field_name = match[1]
    range1 = (int(match[2]), int(match[3]))
    range2 = (int(match[4]), int(match[5]))
    field_ranges[field_name] = (range1, range2)


def parse_your_ticket(line):
    global your_ticket
    your_ticket = parse_ticket(line)


def parse_nearby_ticket(line):
    nearby_tickets.append(parse_ticket(line))


def parse_ticket(line):
    return [int(d) for d in line.split(',')]


parser = parse_field_ranges
for line in lines:
    if line == 'your ticket:':
        parser = parse_your_ticket
    elif line == 'nearby tickets:':
        parser = parse_nearby_ticket
    elif line:
        parser(line)

invalid_values = [v for values in nearby_tickets for v in values if not any(
    r1[0] <= v <= r1[1] or
    r2[0] <= v <= r2[1] for r1, r2 in field_ranges.values())]

print(sum(invalid_values))

valid_tickets = [ticket for ticket in nearby_tickets
                 if not any(v in invalid_values for v in ticket)]

possible_orders = {f: [] for f in field_ranges.keys()}
for field, (r1, r2) in field_ranges.items():
    for column in range(len(field_ranges)):
        if all(r1[0] <= t[column] <= r1[1] or r2[0] <= t[column] <= r2[1]
               for t in valid_tickets):
            possible_orders[field].append(column)

final_order = {}
while len(final_order) < len(field_ranges):
    for field, possibilies in possible_orders.items():
        unassigned_field_indices = [p for p in possibilies
                                    if p not in final_order.values()]
        if len(unassigned_field_indices) == 1:
            final_order[field] = unassigned_field_indices[0]

departure_field_indices = [final_order[f]
                           for f in final_order
                           if f.startswith('departure')]
your_ticket_departure_fields = [your_ticket[i]
                                for i in departure_field_indices]
print(functools.reduce(lambda a, b: a * b, your_ticket_departure_fields))
