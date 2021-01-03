import os
import unittest
import main
import re

TestData = dict[str, tuple[str, str]]

MAIN_FOLDER = '..'


def get_input_files_with_expectations() -> TestData:
    input_file_pattern = re.compile(r'^input.*\.txt$')

    with open(os.path.join(MAIN_FOLDER, 'expected.txt'), 'r') as expect_file:
        lines = expect_file.read().splitlines()

    test_data = {}
    i = 0
    while i < len(lines) - 2:
        line = lines[i]
        if input_file_pattern.match(line):
            test_data[line] = (lines[i + 1],
                               lines[i + 2])
        i += 1
    return test_data


class InputTests(unittest.TestCase):

    def test_all_input_files(self):
        test_data = get_input_files_with_expectations()
        for filename, expectation in test_data.items():
            result = main.main(os.path.join(MAIN_FOLDER, filename))
            self.assertEqual(result[0], expectation[0])
            self.assertEqual(result[1], expectation[1])
