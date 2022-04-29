import unittest
import main
from parameterized import parameterized

EXAMPLE = {0: 3,
           1: 2,
           4: 4,
           6: 4}


class ExampleTests(unittest.TestCase):

    def test_get_total_severity(self):
        self.assertEqual(24, main.get_total_severity(EXAMPLE))

    def test_get_total_severity_uncaught(self):
        self.assertIsNone(main.get_total_severity(EXAMPLE, delay=10))

    def test_find_safe_delay(self):
        self.assertEqual(10, main.find_safe_delay(EXAMPLE))

    @parameterized.expand([
        (0, 3, 0, 0),
        (1, 2, 1, 0),
        (3, 4, 6, 3)
    ])
    def test_calc_step(self, expected, scan_range, delay, time):
        self.assertEqual(expected, main.calc_scan_step(scan_range, delay, time))
