import unittest

from parameterized import parameterized

import main


class ExampleTests(unittest.TestCase):

    @parameterized.expand([
        ([('a', 5), ('b', 3), ('x', 1), ('y', 1), ('z', 1)],
         "aaaaa-bbb-z-y-x"),
        ([('a', 1), ('b', 1), ('c', 1), ('d', 1), ('e', 1)],
         "a-b-c-d-e-f-g-h"),
        ([('o', 3), ('a', 2), ('r', 2), ('e', 1), ('l', 1)],
         "not-a-real-room"),
        ([('l', 3), ('o', 3), ('a', 2), ('r', 2), ('t', 2)],
         "totally-real-room")
    ])
    def test_get_five_most_common(self, expected, room_name):
        self.assertEqual(
            expected,
            main.get_five_most_common(room_name)
        )

    @parameterized.expand([
        (True, "aaaaa-bbb-z-y-x", "abxyz"),
        (True, "a-b-c-d-e-f-g-h", "abcde"),
        (True, "not-a-real-room", "oarel"),
        (False, "totally-real-room", "decoy"),
    ])
    def test_validate(self, expected, name, checksum):
        self.assertEqual(
            expected,
            main.validate(name, checksum)
        )

    def test_solve(self):
        self.assertEqual(
            (1514, 404),
            main.solve([
                "aaaaa-bbb-z-y-x-123[abxyz]",
                "a-b-c-d-e-f-g-h-987[abcde]",
                "not-a-real-room-404[oarel]",
                "totally-real-room-200[decoy]",
            ],
                search='bch o fsoz fcca'
            )
        )

    def test_decipher(self):
        self.assertEqual(
            "very encrypted name",
            main.decipher("qzmt-zixmtkozy-ivhz", 343)
        )

    def test_rotate(self):
        self.assertEqual('v', main.rotate('q', 343))
