import unittest

import main
from main import Round, Stats, Winner


class ExampleTests(unittest.TestCase):

    def test_calc_next_round_1st_example_round_1(self):
        result = main.calc_next_round(
            Round(
                Stats(
                    boss_hp=13,
                    boss_damage=8,
                    player_hp=10,
                    player_mana=250
                ),
                active_spells=[]
            ),
            spell=3,
            hard=False
        )
        self.assertEqual(Winner.NO_ONE, result.winner)
        self.assertEqual(
            Round(
                Stats(
                    boss_hp=10,
                    boss_damage=8,
                    player_hp=2,
                    player_mana=77
                ),
                active_spells=[(3, 5)]
            ),
            result.next_round
        )

    def test_calc_next_round_1st_example_round_2(self):
        result = main.calc_next_round(
            Round(
                Stats(
                    boss_hp=10,
                    boss_damage=8,
                    player_hp=2,
                    player_mana=77
                ),
                active_spells=[(3, 5)]
            ),
            spell=0,
            hard=False)
        self.assertEqual(Winner.PLAYER, result.winner)

    def test_calc_next_round_2nd_example_round_1(self):
        result = main.calc_next_round(
            Round(
                Stats(
                    boss_hp=14,
                    boss_damage=8,
                    player_hp=10,
                    player_mana=250
                ),
                active_spells=[]
            ),
            spell=4,
            hard=False)
        self.assertEqual(Winner.NO_ONE, result.winner)
        self.assertEqual(
            Round(
                Stats(
                    boss_hp=14,
                    boss_damage=8,
                    player_hp=2,
                    player_mana=122
                ),
                active_spells=[(4, 4)]
            ),
            result.next_round
        )

    def test_calc_next_round_2nd_example_round_2(self):
        result = main.calc_next_round(
            Round(
                Stats(
                    boss_hp=14,
                    boss_damage=8,
                    player_hp=2,
                    player_mana=122
                ),
                active_spells=[(4, 4)]
            ),
            spell=2,
            hard=False
        )
        self.assertEqual(Winner.NO_ONE, result.winner)
        self.assertEqual(
            Round(
                Stats(
                    boss_hp=14,
                    boss_damage=8,
                    player_hp=1,
                    player_mana=211
                ),
                active_spells=[(4, 2), (2, 5)]
            ),
            result.next_round
        )

    def test_calc_next_round_2nd_example_round_3(self):
        result = main.calc_next_round(
            Round(
                Stats(
                    boss_hp=14,
                    boss_damage=8,
                    player_hp=1,
                    player_mana=211
                ),
                active_spells=[(4, 2), (2, 5)]
            ),
            spell=1,
            hard=False
        )
        self.assertEqual(Winner.NO_ONE, result.winner)
        self.assertEqual(
            Round(
                Stats(
                    boss_hp=12,
                    boss_damage=8,
                    player_hp=2,
                    player_mana=340
                ),
                active_spells=[(2, 3)]
            ),
            result.next_round
        )

    def test_calc_next_round_2nd_example_round_4(self):
        result = main.calc_next_round(
            Round(
                Stats(
                    boss_hp=12,
                    boss_damage=8,
                    player_hp=2,
                    player_mana=340
                ),
                active_spells=[(2, 3)]
            ),
            spell=3,
            hard=False
        )
        self.assertEqual(Winner.NO_ONE, result.winner)
        self.assertEqual(
            Round(
                Stats(
                    boss_hp=9,
                    boss_damage=8,
                    player_hp=1,
                    player_mana=167
                ),
                active_spells=[(2, 1), (3, 5)]
            ),
            result.next_round
        )

    def test_calc_next_round_2nd_example_round_5(self):
        result = main.calc_next_round(
            Round(
                Stats(
                    boss_hp=9,
                    boss_damage=8,
                    player_hp=1,
                    player_mana=167
                ),
                active_spells=[(2, 1), (3, 5)]
            ),
            spell=0,
            hard=False
        )
        self.assertEqual(Winner.PLAYER, result.winner)
        self.assertEqual(114, result.mana)

    def test_solve_example_1(self):
        self.assertEqual(
            226,
            main.solve(
                Stats(
                    boss_hp=13,
                    boss_damage=8,
                    player_hp=10,
                    player_mana=250,
                ),
                hard=False
            )
        )

    def test_solve_example_2(self):
        self.assertEqual(
            641,
            main.solve(
                Stats(
                    boss_hp=14,
                    boss_damage=8,
                    player_hp=10,
                    player_mana=250,
                ),
                hard=False
            )
        )

    def test_solve_55_8(self):
        self.assertEqual(
            953,
            main.solve(
                Stats(
                    boss_hp=55,
                    boss_damage=8,
                    player_hp=50,
                    player_mana=500,
                ),
                hard=False
            )
        )

    def test_solve_71_10(self):
        self.assertEqual(
            1824,
            main.solve(
                Stats(
                    boss_hp=71,
                    boss_damage=10,
                    player_hp=50,
                    player_mana=500,
                ),
                hard=False
            )
        )
