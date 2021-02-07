import re
import json
from typing import Union

PATTERN = re.compile(r'-?\d+')


def clean(document: Union[str, list, dict]) -> Union[str, list, dict]:
    if isinstance(document, (str, int)):
        return document
    elif isinstance(document, list):
        return [clean(element) for element in document]
    elif isinstance(document, dict):
        result = {}
        for k, v in document.items():
            if v != 'red':
                result[k] = clean(v)
            else:
                return ""
        return result


def solve(content: str) -> int:
    match = PATTERN.findall(content)
    return sum(int(d) for d in match)


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        content = fp.read()
    sum_of_all = solve(content)
    cleaned = json.dumps(clean(json.loads(content)))
    sum_of_non_red = solve(cleaned)
    return sum_of_all, sum_of_non_red


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
