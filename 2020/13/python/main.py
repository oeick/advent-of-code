from time import time
from math import ceil

eta = 1000677
ids = '29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,661,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,521,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19'
# ids = '7,13,x,x,59,x,31,19'
# ids = '1789,37,47,1889'

# --------- Part 1 --------

known_ids = [int(d) for d in ids.split(',') if d != 'x']
waiting_t = [ceil(eta/i) * i - eta for i in known_ids]

shortest_waiting_time = min(waiting_t)
next_bus = known_ids[waiting_t.index(shortest_waiting_time)]

print(next_bus * shortest_waiting_time)

# -------- Part 2 ---------

start_value = 100000000000000
# start_value = 0

id_list = [(p, int(i)) for p, i in enumerate(ids.split(',')) if i != 'x']

max_id_index, max_id_value = max(id_list, key=lambda i: i[1])

id_list_relative = [(i-max_id_index, v) for i, v in id_list]
id_list_rel_sort = sorted(id_list_relative, key=lambda x: x[1], reverse=True)

print(id_list_rel_sort)

relative_t = [start_value//i[1]*i[1] for i in id_list_rel_sort]

check_t = time()
while True:
    relative_t[0] += id_list_rel_sort[0][1]
    for n, id_and_val in enumerate(id_list_rel_sort[1:], start=1):
        i, v = id_and_val
        while relative_t[n] < relative_t[0] + i:
            relative_t[n] += v
        if relative_t[n] > relative_t[0] + i:
            break
    else:
        break
    if time() > check_t + 10:
        print(relative_t)
        check_t = time()
print(relative_t)
print(min(relative_t))
