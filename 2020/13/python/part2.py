# trying an other idea for part 2
# - *much* faster than the old brute force (< 1s)
# - no complicated math required
# seems to work, needs cleanup

def find_next_valid_bus(prev_hit, prev_period, new_dist, new_bus):
    """
    prev_hit: when the previous busses met the condition
    prev_period: period of the condition of the previous busses
    new_dist: how minutes after the 1st bus the new bus must depart
    new_bus: id number of the new bus
    """
    minute = prev_hit
    while (minute + new_dist) % new_bus != 0:
        minute += prev_period
    return minute


def find_next_period(prev_hit, prev_period, new_dist, new_bus):
    first_hit = find_next_valid_bus(prev_hit, prev_period, new_dist, new_bus)
    second_hit = find_next_valid_bus(first_hit + prev_period, prev_period, new_dist, new_bus)
    return first_hit, second_hit - first_hit


ids = '29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,661,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,521,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19'
busses = [(p, int(i)) for p, i in enumerate(ids.split(',')) if i != 'x']
minute_hit, period_hit = 2, 2
for dist, bus_id in busses:
    minute_hit, period_hit = find_next_period(minute_hit, period_hit, dist, bus_id)
print(minute_hit)


# ascii visualization for testing with smaller examples:

# s = ['.'] * (busses[-1][0] + 1)
# for b in busses:
#     s[b[0]] = '{}'
# s = ''.join(s)

# for n in range(m, m + busses[-1][0] + 1):
#     s2 = s.format(*['X' if n % b[1] == 0 else '.' for i, b in enumerate(busses)])
#     print('{:04} '.format(n) + s2)
