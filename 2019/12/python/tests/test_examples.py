import unittest

import main
from moon import Moon


class MoonTests(unittest.TestCase):

    def test_update_velocity(self):
        moon_a = Moon(name='A', pos=[0, 0, 0])
        moon_b = Moon(name='B', pos=[9, 9, 9])
        self.assertEqual(
            [[1, 1, 1], [-1, -1, -1]],
            [m.vel for m in main.update_velocity([moon_a, moon_b])])

    def test_update_position(self):
        moon_a = Moon(name='A', pos=[0, 0, 0], vel=[1, 1, 1])
        moon_b = Moon(name='B', pos=[9, 9, 9], vel=[-1, -1, -1])
        self.assertEqual(
            [[1, 1, 1], [8, 8, 8]],
            [m.pos for m in main.update_position([moon_a, moon_b])])

    def test_step_moons(self):
        moon_a = Moon(name='A', pos=[0, 9, 0], vel=[0, 0, 0])
        moon_b = Moon(name='B', pos=[9, 0, 9], vel=[1, 2, 3])
        self.assertEqual(
            [([1, 8, 1], [1, -1, 1]),
             ([9, 3, 11], [0, 3, 2])],
            [(m.pos, m.vel) for m in main.step_moons([moon_a, moon_b])])

    def test_simulate_moons(self):
        self.assertEqual(
            [Moon(name='I', pos=[2, 1, -3], vel=[-3, -2, 1]),
             Moon(name='E', pos=[1, -8, 0], vel=[-1, 1, 3]),
             Moon(name='G', pos=[3, -6, 1], vel=[3, 2, -3]),
             Moon(name='C', pos=[2, 0, 4], vel=[1, -1, -1])],
            main.simulate_moons(
                [Moon(name='I', pos=[-1, 0, 2]),
                 Moon(name='E', pos=[2, -10, -7]),
                 Moon(name='G', pos=[4, -8, 8]),
                 Moon(name='C', pos=[3, 5, -1])],
                steps=10))

    def test_calc_total_energy(self):
        self.assertEqual(
            179,
            main.calc_total_energy(
                [Moon(name='I', pos=[2, 1, -3], vel=[-3, -2, 1]),
                 Moon(name='E', pos=[1, -8, 0], vel=[-1, 1, 3]),
                 Moon(name='G', pos=[3, -6, 1], vel=[3, 2, -3]),
                 Moon(name='C', pos=[2, 0, 4], vel=[1, -1, -1])]))
