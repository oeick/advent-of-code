import re

inner_bracket_pattern = re.compile(r'.*(\(.+?\)).*')
left_simple_expression = re.compile(r'(\d+ .? \d+).*')
left_advanced_expression = re.compile(r'.*?(\d+ \+ \d+).*?')

with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file]


def calc_simple(string):
    while '+' in string or '*' in string:
        match = left_simple_expression.match(string)
        result = eval(match[1])
        string = string.replace(match[1], str(result), 1)
    return string


def calc_advanced(string):
    while '+' in string:
        match = left_advanced_expression.match(string)
        result = eval(match[1])
        string = string.replace(match[1], str(result), 1)
    return calc_simple(string)


def replace_innermost_bracket(string, calculator):
    match = inner_bracket_pattern.match(string)
    bracket = match[1]
    calculated = calculator(bracket[1:-1])
    return string.replace(bracket, calculated)


def replace_all_brackets(string, calculator):
    while '(' in string:
        string = replace_innermost_bracket(string, calculator)
    return string


def solve_simple(input_strings):
    results = [int(calc_simple(replace_all_brackets(line, calc_simple)))
               for line in input_strings]
    return sum(results)


def solve_advanced(input_strings):
    results = [int(calc_advanced(replace_all_brackets(line, calc_advanced)))
               for line in input_strings]
    return sum(results)


print(solve_simple(lines))
print(solve_advanced(lines))
