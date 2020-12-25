from itertools import combinations

with open('input.txt', 'r') as fp:
    numbers = [int(line.strip()) for line in fp]

preamble = 25

for i, number in enumerate(numbers[preamble:]):
    sums = [sum(c) for c in combinations(numbers[i:i+preamble], 2)]
    if number not in sums:
        print(number)
        break

for size in range(2, len(numbers)+1):
    for i in range(len(numbers)-size+1):
        window = numbers[i:i+size]
        if sum(window) == number:
            print(min(window) + max(window))
