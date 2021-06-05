import unittest

import main
from main import Item, Stats


class ExampleTests(unittest.TestCase):

    def test_calculate_player_stats(self):
        self.assertEqual(
            Stats(
                hp=100,
                damage=3,
                armor=30
            ),
            main.calculate_player_stats({
                Item(damage=1),
                Item(damage=2),
                Item(armor=10),
                Item(armor=20),
            })
        )

    def test_fight_from_example(self):
        player_stats = Stats(
            hp=8,
            damage=5,
            armor=5,
        )
        boss_stats = Stats(
            hp=12,
            damage=7,
            armor=2,
        )
        self.assertTrue(main.fight(player_stats, boss_stats))
