import unittest

import computer


class ExampleTests(unittest.TestCase):

    def test_example_1(self):
        cmp = computer.Computer(
            {0: 109, 1: 1, 2: 204, 3: -1, 4: 1001, 5: 100,
             6: 1, 7: 100, 8: 1008, 9: 100, 10: 16,
             11: 101, 12: 1006, 13: 101, 14: 0, 15: 99},
            [])
        result = []
        while (out := cmp.run()) is not None:
            result.append(out)
        self.assertEqual([109, 1, 204, -1, 1001, 100, 1, 100,
                          1008, 100, 16, 101, 1006, 101, 0, 99],
                         result)

    def test_example_2(self):
        cmp = computer.Computer(
            {0: 1102, 1: 34915192, 2: 34915192, 3: 7, 4: 4, 5: 7, 6: 99, 7: 0},
            [])
        self.assertEqual(16, len(str(cmp.run())))

    def test_example_3(self):
        cmp = computer.Computer({0: 104, 1: 1125899906842624, 2: 99}, [])
        self.assertEqual(1125899906842624, cmp.run())

    def test_add(self):
        cmp = computer.Computer({0: 1001, 1: 5, 2: 1, 3: 5, 4: 99, 5: 3}, [])
        cmp.run()
        cmp.instr_pointer = 0
        cmp.run()
        self.assertEqual({0: 1001, 1: 5, 2: 1, 3: 5, 4: 99, 5: 5}, cmp.program)
