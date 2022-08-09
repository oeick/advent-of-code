import unittest

import main


class ExampleTests(unittest.TestCase):

    def test_example(self):
        lines = ['COM)B',
                 'B)C',
                 'C)D',
                 'D)E',
                 'E)F',
                 'B)G',
                 'G)H',
                 'D)I',
                 'E)J',
                 'J)K',
                 'K)L',
                 'K)YOU',
                 'I)SAN']
        orbitmap = main.parse_orbitmap(lines)
        centermap = main.create_centermap(orbitmap)
        self.assertEqual((54, 4), main.solve(centermap))
