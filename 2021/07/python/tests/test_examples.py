import unittest
from parameterized import parameterized
from main import get_cheap_fuel, get_expensive_fuel

EXAMPLE = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


class ExampleTests(unittest.TestCase):
    @parameterized.expand([
        (41, 1, get_cheap_fuel),
        (37, 2, get_cheap_fuel),
        (39, 3, get_cheap_fuel),
        (71, 10, get_cheap_fuel),
        (206, 2, get_expensive_fuel),
        (168, 5, get_expensive_fuel),
    ])
    def test_get_fuel_at_position_1(self, fuel, position, method):
        self.assertEqual(fuel, method(EXAMPLE, position))
