import re
from typing import Dict

with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file]

rules: Dict[str, str] = {}
messages = []
for line in lines:
    if ':' in line:
        number, text = line.split(':')
        rules[number] = text + ' '
    elif line:
        messages.append(line)


num_pattern = re.compile(r' (\d+) ')

while True:
    match = num_pattern.search(rules['0'])
    if match:
        number = match[1]
        rule = rules[number]
        if '|' in rule:
            rule = f' ({rule}) '
        rules['0'] = rules['0'].replace(f' {number} ', rule)
    else:
        break

final_rule = rules['0'].replace(' ', '').replace('"', '')

validity_pattern = re.compile(f'^{final_rule}$')

valid_messages = [m for m in messages if validity_pattern.match(m)]

print(len(valid_messages))
