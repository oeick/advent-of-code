import unittest
import main


class ExampleTests(unittest.TestCase):

    def test_empty_string(self):
        self.assertFalse(main.is_nice1(''))
        self.assertFalse(main.is_nice2(''))

    def test_examples_part_1_nice(self):
        self.assertTrue(main.is_nice1('ugknbfddgicrmopn'))
        self.assertTrue(main.is_nice1('aaa'))

    def test_examples_part_1_naughty(self):
        self.assertFalse(main.is_nice1('jchzalrnumimnmhp'))
        self.assertFalse(main.is_nice1('haegwjzuvuyypxyu'))
        self.assertFalse(main.is_nice1('dvszwmarrgswjxmb'))

    def test_examples_part_2_nice(self):
        self.assertTrue(main.is_nice2('qjhvhtzxzqqjkmpb'))
        self.assertTrue(main.is_nice2('xxyxx'))

    def test_examples_part_2_naughty(self):
        self.assertFalse(main.is_nice2('uurcxstgmygtbstg'))
        self.assertFalse(main.is_nice2('ieodomkazucvgmuy'))

    def test_list_of_strings1(self):
        lines = ['ugknbfddgicrmopn',
                 'aaa',
                 'jchzalrnumimnmhp']
        nice_lines = main.get_nice_lines1(lines)
        self.assertEqual(['ugknbfddgicrmopn', 'aaa'], nice_lines)

    def test_list_of_strings2(self):
        lines = ['qjhvhtzxzqqjkmpb',
                 'xxyxx',
                 'uurcxstgmygtbstg']
        nice_lines = main.get_nice_lines2(lines)
        self.assertEqual(['qjhvhtzxzqqjkmpb', 'xxyxx'], nice_lines)
