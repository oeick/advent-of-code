import unittest
import main


class ExampleTests(unittest.TestCase):

    def test_example(self):
        example = """
        London to Dublin = 464
        London to Belfast = 518
        Dublin to Belfast = 141
        """
        lines = [line.strip() for line in example.splitlines() if line.strip()]
        distances = main.parse_distances(lines)
        shortest, longest = main.solve(distances)
        self.assertEqual(605, shortest)
        self.assertEqual(982, longest)
