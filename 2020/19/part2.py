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


def get_partial_rule(root: str, base_rules: Dict[str, str]):
    rules: Dict[str, str] = dict(base_rules)
    while True:
        match = num_pattern.search(rules[root])
        if match:
            number = match[1]
            rule = rules[number]
            if '|' in rule:
                rule = f' ({rule}) '
            rules[root] = rules[root].replace(f' {number} ', rule)
        else:
            break
    final_rule = rules[root].replace(' ', '').replace('"', '')
    return final_rule


rule42 = get_partial_rule('42', rules)
rule31 = get_partial_rule('31', rules)

secondary_rule = f'^({rule42}){{2,}}({rule31}){{1,}}$'
secondary_pattern = re.compile(secondary_rule)

filtered_messages = [m for m in messages if secondary_pattern.fullmatch(m)]

primary_rules = ['^' + f'({rule42})' * j + f'({rule31})' * i + '$'
                 for i in range(6) for j in range(i+1, 11)]

primary_patterns = [re.compile(r) for r in primary_rules]

valid_messages = [fm for fm in filtered_messages
                  if any(pp.fullmatch(fm) for pp in primary_patterns)]

print(len(valid_messages))
