import unittest
import main


class ExampleTests(unittest.TestCase):

    def test_example(self):
        ingredients = main.parse_ingredients([
            'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
            'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'])

        self.assertEqual({
            'Butterscotch': {
                'calories': 8,
                'capacity': -1,
                'durability': -2,
                'flavor': 6,
                'texture': 3},
            'Cinnamon': {
                'calories': 3,
                'capacity': 2,
                'durability': 3,
                'flavor': -2,
                'texture': -1}},
            ingredients)

    def test_calc_score(self):
        result = main.solve({
            'Butterscotch': {
                'calories': 8,
                'capacity': -1,
                'durability': -2,
                'flavor': 6,
                'texture': 3},
            'Cinnamon': {
                'calories': 3,
                'capacity': 2,
                'durability': 3,
                'flavor': -2,
                'texture': -1}})
        self.assertEqual((62842880, 0), result)
