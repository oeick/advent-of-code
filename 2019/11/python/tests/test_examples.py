import unittest
from main import Direction, Position, Robot


class BasicTests(unittest.TestCase):

    def test_direction_turn_by_code(self):
        self.assertEqual(Direction.WEST, Direction.NORTH.turn(0))

    def test_direction_turn(self):
        self.assertEqual(Direction.EAST, Direction.NORTH.turn_right())

    def test_robot_move(self):
        robot = Robot(Position(0, 0), Direction.SOUTH)
        robot.move()
        self.assertEqual((0, 1), robot.position)
