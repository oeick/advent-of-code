import unittest
import main

TESTDATA = """
initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #
""".splitlines()[1:]


class ExampleTests(unittest.TestCase):

    def test_example(self):
        result = main.solve(TESTDATA)
        self.assertEqual((325, 999999999374), result)
