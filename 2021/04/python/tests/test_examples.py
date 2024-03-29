import unittest

import main


class ExampleTests(unittest.TestCase):

    def test_parse_boards(self):
        self.assertEqual(
            [
                [[22, 13, 17, 11, 0],
                 [8, 2, 23, 4, 24],
                 [21, 9, 14, 16, 7],
                 [6, 10, 3, 18, 5],
                 [1, 12, 20, 15, 19]],
                [[3, 15, 0, 2, 22],
                 [9, 18, 13, 17, 5],
                 [19, 8, 7, 25, 23],
                 [20, 11, 10, 24, 4],
                 [14, 21, 16, 12, 6]],
                [[14, 21, 17, 24, 4],
                 [10, 16, 15, 9, 19],
                 [18, 8, 23, 26, 20],
                 [22, 11, 13, 6, 5],
                 [2, 0, 12, 3, 7]]
            ],
            main.parse_boards([
                '',
                '22 13 17 11  0',
                ' 8  2 23  4 24',
                '21  9 14 16  7',
                ' 6 10  3 18  5',
                ' 1 12 20 15 19',
                '',
                ' 3 15  0  2 22',
                ' 9 18 13 17  5',
                '19  8  7 25 23',
                '20 11 10 24  4',
                '14 21 16 12  6',
                '',
                '14 21 17 24  4',
                '10 16 15  9 19',
                '18  8 23 26 20',
                '22 11 13  6  5',
                ' 2  0 12  3  7', ]))

    def test_mark_number(self):
        board = [[22, 13, 17, 11, 0],
                 [8, 2, 23, 4, 24],
                 [21, 9, 14, 16, 7],
                 [6, 10, 3, 18, 5],
                 [1, 12, 20, 15, 19]]
        main.mark_number(board, 24)
        self.assertEqual(
            [[22, 13, 17, 11, 0],
             [8, 2, 23, 4, -1],
             [21, 9, 14, 16, 7],
             [6, 10, 3, 18, 5],
             [1, 12, 20, 15, 19]],
            board)

    def test_has_board_won_FALSE(self):
        self.assertFalse(
            main.has_board_won([
                [22, 13, 17, 11, 0],
                [8, 2, 23, 4, 24],
                [21, 9, 14, 16, 7],
                [6, 10, 3, 18, 5],
                [1, 12, 20, 15, 19]]))

    def test_has_board_won_LINE_COMPLETED(self):
        self.assertTrue(
            main.has_board_won([
                [22, 13, 17, 11, 0],
                [-1, -1, -1, -1, -1],
                [21, 9, 14, 16, 7],
                [6, 10, 3, 18, 5],
                [1, 12, 20, 15, 19]]))

    def test_has_board_won_COLUMN_COMPLETED(self):
        self.assertTrue(
            main.has_board_won([
                [22, 13, 17, -1, 0],
                [8, 2, 23, -1, 24],
                [21, 9, 14, -1, 7],
                [6, 10, 3, -1, 5],
                [1, 12, 20, -1, 19]]))

    def test_sum_unmarked(self):
        self.assertEqual(
            188,
            main.sum_unmarked([
                [-1, -1, -1, -1, -1],
                [10, 16, 15, -1, 19],
                [18, 8, -1, 26, 20],
                [22, -1, 13, 6, -1],
                [-1, -1, 12, 3, -1]])
        )

    def test_solve(self):
        self.assertEqual(
            (4512, 1924),
            main.solve(
                [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1],
                [
                    [[22, 13, 17, 11, 0],
                     [8, 2, 23, 4, 24],
                     [21, 9, 14, 16, 7],
                     [6, 10, 3, 18, 5],
                     [1, 12, 20, 15, 19]],
                    [[3, 15, 0, 2, 22],
                     [9, 18, 13, 17, 5],
                     [19, 8, 7, 25, 23],
                     [20, 11, 10, 24, 4],
                     [14, 21, 16, 12, 6]],
                    [[14, 21, 17, 24, 4],
                     [10, 16, 15, 9, 19],
                     [18, 8, 23, 26, 20],
                     [22, 11, 13, 6, 5],
                     [2, 0, 12, 3, 7]]
                ]))
