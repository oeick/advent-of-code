import re


def parse_passport(lines):
    separated_fields = [s.split(':') for line in lines for s in line.split()]
    return {k: v for k, v in separated_fields}


def validation(pp, enhanced=False):
    if any(f not in pp for f in
           ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
        return False

    if not enhanced:
        return True

    if (
            not 1920 <= int(pp['byr']) <= 2002 or
            not 2010 <= int(pp['iyr']) <= 2020 or
            not 2020 <= int(pp['eyr']) <= 2030):
        return False

    if pp['hgt'][-2:] == 'in':
        if not 59 <= int(pp['hgt'][:-2]) <= 76:
            return False
    elif pp['hgt'][-2:] == 'cm':
        if not 150 <= int(pp['hgt'][:-2]) <= 193:
            return False
    else:
        return False

    if not re.match('^#[0-9a-f]{6}$', pp['hcl']):
        return False

    if pp['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    if not re.match(r'^\d{9}$', pp['pid']):
        return False

    return True


def solve(batch_lines):
    counter1, counter2 = 0, 0
    passport_lines = []
    for line in batch_lines + ['']:
        if line:
            passport_lines.append(line)
        else:
            passport = parse_passport(passport_lines)
            if validation(passport):
                counter1 += 1
            if validation(passport, enhanced=True):
                counter2 += 1
            passport_lines = []
    return counter1, counter2


def main(filename):
    with open(filename, 'r') as fp:
        batch_lines = fp.read().splitlines()
    return solve(batch_lines)


if __name__ == '__main__':
    solution1, solution2 = main('input.txt')
    print(solution1)
    print(solution2)
