import unittest

from parameterized import parameterized

import main
from main import Node


def _verify_integrity(node: Node):
    current = node
    while current.next:
        if current.next.prev != current:
            return False
        current = current.next
    return True


class ExampleTests(unittest.TestCase):

    def test_parse_chars(self):
        first_node = main.parse_chars('[12]')
        self.assertEqual(-1, first_node.value)
        self.assertEqual(1, first_node.next.value)
        self.assertEqual(2, first_node.next.next.value)
        self.assertEqual(-3, first_node.next.next.next.value)

    @parameterized.expand([
        (9, '[[[[[98]1]2]3]4]'),
        (3, '[7[6[5[4[32]]]]]'),
        (3, '[[6[5[4[32]]]]1]'),
        (7, '[[3[2[1[73]]]][6[5[4[32]]]]]'),
        (3, '[[3[2[80]]][9[5[4[32]]]]]')])
    def test_find_bomb(self, expected, chars):
        self.assertEqual(
            expected, main.find_bomb(main.parse_chars(chars)).value)

    def test_node_repr(self):
        self.assertEqual(
            '[[[[[98]1]2]3]4]', str(main.parse_chars('[[[[[98]1]2]3]4]')))

    @parameterized.expand([
        ('[[[[09]2]3]4]', '[[[[[98]1]2]3]4]'),
        ('[7[6[5[70]]]]', '[7[6[5[4[32]]]]]'),
        ('[[6[5[70]]]3]', '[[6[5[4[32]]]]1]'),
        ('[[3[2[80]]][9[5[4[32]]]]]', '[[3[2[1[73]]]][6[5[4[32]]]]]'),
        ('[[3[2[80]]][9[5[70]]]]', '[[3[2[80]]][9[5[4[32]]]]]'),
    ])
    def test_explode(self, expected, chars):
        first = main.parse_chars(chars)
        main.explode(main.find_bomb(first))
        self.assertEqual(expected, str(first))

    def test_split(self):
        first = main.parse_chars('[20]')
        first.next.next.value = 11
        splittable = main.find_splittable(first)
        self.assertEqual(11, splittable.value)
        main.split(splittable)
        self.assertEqual('[2[56]]', str(first))

    def test_find_last(self):
        first = main.parse_chars('[12]')
        self.assertEqual(-3, main.find_last(first).value)

    def test_add(self):
        first = main.parse_chars('[12]')
        summand = main.parse_chars('[[34]5]')
        main.add(first, summand)
        self.assertEqual('[[12][[34]5]]', str(first.prev))
        self.assertTrue(_verify_integrity(first.prev))

    def test_example_step_by_step(self):
        first = main.parse_chars('[[[[43]4]4][7[[84]9]]]')
        first = main.add(first, main.parse_chars('[11]'))
        main.explode(main.find_bomb(first))
        main.explode(main.find_bomb(first))
        main.split(main.find_splittable(first))
        main.split(main.find_splittable(first))
        main.explode(main.find_bomb(first))
        self.assertEqual('[[[[07]4][[78][60]]][81]]', str(first))

    def test_reduce(self):
        first = main.parse_chars('[[[[[43]4]4][7[[84]9]]][11]]')
        main.reduce_node(first)
        self.assertEqual('[[[[07]4][[78][60]]][81]]', str(first))

    def test_add_list_1(self):
        list_of_nodes = [
            main.parse_chars('[11]'),
            main.parse_chars('[22]'),
            main.parse_chars('[33]'),
            main.parse_chars('[44]')]
        first = main.add_list(list_of_nodes)
        self.assertEqual('[[[[11][22]][33]][44]]', str(first))

    def test_add_list_2(self):
        list_of_nodes = [
            main.parse_chars('[11]'),
            main.parse_chars('[22]'),
            main.parse_chars('[33]'),
            main.parse_chars('[44]'),
            main.parse_chars('[55]')]
        first = main.add_list(list_of_nodes)
        self.assertEqual('[[[[30][53]][44]][55]]', str(first))

    def test_add_list_3(self):
        list_of_nodes = [
            main.parse_chars('[11]'),
            main.parse_chars('[22]'),
            main.parse_chars('[33]'),
            main.parse_chars('[44]'),
            main.parse_chars('[55]'),
            main.parse_chars('[66]')]
        first = main.add_list(list_of_nodes)
        self.assertEqual('[[[[50][74]][55]][66]]', str(first))

    def test_add_list_large(self):
        list_of_nodes = [
            main.parse_chars('[[[0[45]][00]][[[45][26]][95]]]'),
            main.parse_chars('[7[[[37][43]][[63][88]]]]'),
            main.parse_chars('[[2[[08][34]]][[[67]1][7[16]]]]'),
            main.parse_chars('[[[[24]7][6[05]]][[[68][28]][[21][45]]]]'),
            main.parse_chars('[7[5[[38][14]]]]'),
            main.parse_chars('[[2[22]][8[81]]]'),
            main.parse_chars('[29]'),
            main.parse_chars('[1[[[93]9][[90][07]]]]'),
            main.parse_chars('[[[5[74]]7]1]'),
            main.parse_chars('[[[[42]2]6][87]]')]
        first = main.add_list(list_of_nodes)
        self.assertEqual('[[[[87][77]][[86][77]]][[[07][66]][87]]]', str(first))

    def test_large_step_1(self):
        first = main.parse_chars('[[[0[45]][00]][[[45][26]][95]]]')
        summand = main.parse_chars('[7[[[37][43]][[63][88]]]]')
        first = main.add(first, summand)
        main.reduce_node(first)
        _verify_integrity(first)
        self.assertEqual(
            '[[[[40][54]][[77][60]]][[8[77]][[79][50]]]]',
            str(first))

    def test_debug(self):
        first = main.parse_chars(
            '[[[[40][54]][[77][60]]][[8[45]][[[56]9][90]]]]')
        bomb = main.find_bomb(first)
        main.explode(bomb)
        self.assertEqual(
            '[[[[40][54]][[77][60]]][[8[4A]][[0F][90]]]]', str(first))

    @parameterized.expand([
        (29, '[91]'),
        (129, '[[91][19]]'),
        (143, '[[12][[34]5]]'),
        (1384, '[[[[07]4][[78][60]]][81]]'),
        (445, '[[[[11][22]][33]][44]]'),
        (791, '[[[[30][53]][44]][55]]'),
        (1137, '[[[[50][74]][55]][66]]'),
        (3488, '[[[[87][77]][[86][77]]][[[07][66]][87]]]')])
    def test_magnitude(self, expected, chars):
        first = main.parse_chars(chars)
        self.assertEqual(expected, main.calc_magnitude(first))

    def test_part_1_example_homework_assignment(self):
        homework = """
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
""".strip().splitlines()
        nodes = main.parse_input(homework)
        first = main.add_list(nodes)
        self.assertEqual(
            '[[[[66][76]][[77][70]]][[[77][77]][[78][99]]]]', str(first))
        self.assertEqual(4140, main.calc_magnitude(first))

    def test_part_2_example_homework_assignment(self):
        homework = """
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
""".strip().splitlines()
        nodes = main.parse_input(homework)
        self.assertEqual(3993, main.solve_part_2(nodes))
