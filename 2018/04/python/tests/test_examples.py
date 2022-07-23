import unittest
from itertools import chain

import main


class ExampleTests(unittest.TestCase):

    def test_get_guard_sleep_minutes(self):
        self.assertEqual({
            10: list(chain(range(5, 25), range(30, 55), range(24, 29))),
            99: list(chain(range(40, 50), range(36, 46), range(45, 55)))
        }, main.get_guard_sleep_minutes([
            '[1518-11-01 00:00] Guard #10 begins shift',
            '[1518-11-01 00:05] falls asleep',
            '[1518-11-01 00:25] wakes up',
            '[1518-11-01 00:30] falls asleep',
            '[1518-11-01 00:55] wakes up',
            '[1518-11-01 23:58] Guard #99 begins shift',
            '[1518-11-02 00:40] falls asleep',
            '[1518-11-02 00:50] wakes up',
            '[1518-11-03 00:05] Guard #10 begins shift',
            '[1518-11-03 00:24] falls asleep',
            '[1518-11-03 00:29] wakes up',
            '[1518-11-04 00:02] Guard #99 begins shift',
            '[1518-11-04 00:36] falls asleep',
            '[1518-11-04 00:46] wakes up',
            '[1518-11-05 00:03] Guard #99 begins shift',
            '[1518-11-05 00:45] falls asleep',
            '[1518-11-05 00:55] wakes up']))

    def test_solve_part_1(self):
        self.assertEqual(
            240,
            main.solve_part_1({
                10: list(chain(range(5, 25), range(30, 55), range(24, 29))),
                99: list(chain(range(40, 50), range(36, 46), range(45, 55)))
            }))

    def test_solve_part_2(self):
        self.assertEqual(
            4455,
            main.solve_part_2({
                10: list(chain(range(5, 25), range(30, 55), range(24, 29))),
                99: list(chain(range(40, 50), range(36, 46), range(45, 55)))
            }))
