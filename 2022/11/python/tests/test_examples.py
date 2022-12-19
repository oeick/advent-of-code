import unittest

import main

EXAMPLE: list[str] = """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""".splitlines()[1:]


class ExampleTests(unittest.TestCase):

    def test_example_part_1(self):
        result = main.solve(main.parse_monkeys(EXAMPLE), 20, lambda w: w // 3)
        self.assertEqual(10605, result)

    def test_example_part_2(self):
        monkeys = main.parse_monkeys(EXAMPLE)
        result = main.solve(monkeys,
                            10_000,
                            lambda w: w % main.multiply_divisors(monkeys))
        self.assertEqual(2713310158, result)
