import re

with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file]

mem_pattern = re.compile(r'mem\[(\d+)] = (\d+)')

memory = {}
mask_and, mask_or = 0, 0

for line in lines:
    if line.startswith('mask'):
        mask = line[7:]
        mask_and = int(''.join(['1' if b == 'X' else b for b in mask]), 2)
        mask_or = int(''.join(['0' if b == 'X' else b for b in mask]), 2)
    elif line.startswith('mem'):
        match = mem_pattern.match(line)
        address, value = int(match[1]), int(match[2])
        memory[address] = value & mask_and | mask_or

print(sum(memory.values()))

memory = {}
mask = []
for line in lines:
    if line.startswith('mask'):
        mask = list(line[7:])
        mask_or = int(''.join(['0' if b == 'X' else b for b in mask]), 2)
    elif line.startswith('mem'):
        match = mem_pattern.match(line)
        address, value = int(match[1]), int(match[2])
        placeholders = [i for i, b in enumerate(mask) if b == 'X']
        masked_address = address | mask_or
        addresses = set()
        for replacement_bits in range(2**len(placeholders)):
            replacement_bits_str = '{:0{}b}'.format(
                replacement_bits, len(placeholders))
            new_address = list('{:036b}'.format(masked_address))
            for i in range(len(placeholders)):
                new_address[placeholders[i]] = replacement_bits_str[i]
            addresses.add(int(''.join(new_address), 2))
        for a in addresses:
            memory[a] = value

print(sum(memory.values()))
