import unittest

import main
from main import Dir, File

EXAMPLE = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".splitlines()[1:]


class ExampleTests(unittest.TestCase):

    def test_parse_tree_flat(self):
        self.assertEqual(
            Dir.of(name='/',
                   files=[File('b.txt', 14848514), File('c.dat', 8504156)],
                   subdir_names=['a', 'd']),
            main.parse_tree([
                '$ cd /',
                '$ ls',
                'dir a',
                '14848514 b.txt',
                '8504156 c.dat',
                'dir d']))

    def test_parse_tree_depth(self):
        self.assertEqual(
            Dir(name='/',
                files={},
                subs={
                    'a': Dir.of(name='a',
                                files=[File('f.txt', 1)],
                                subdir_names=['v', 'w']),
                    'b': Dir.of(name='b',
                                files=[File('g.txt', 2)],
                                subdir_names=['x', 'y'])}),
            main.parse_tree([
                '$ cd /',
                '$ ls',
                'dir a',
                'dir b',
                '$ cd a',
                '$ ls',
                'dir v',
                'dir w',
                '1 f.txt',
                '$ cd /',
                '$ cd b',
                '$ ls',
                'dir x',
                'dir y',
                '2 g.txt']))

    def test_calc_total_size_flat(self):
        self.assertEqual(
            46,
            main.parse_tree([
                '$ cd /',
                '$ ls',
                '12 b.txt',
                '34 c.dat']).calc_total_size())

    def test_calc_total_size_depth(self):
        self.assertEqual(
            68,
            main.parse_tree([
                '$ cd /',
                '$ ls',
                '12 b.txt',
                'dir a',
                '$ cd a',
                '$ ls',
                '56 c.txt'
            ]).calc_total_size())

    def test_example_tree(self):
        tree = main.parse_tree(EXAMPLE)
        self.assertEqual(
            Dir(name='/',
                files={'b.txt': File('b.txt', 14848514),
                       'c.dat': File('c.dat', 8504156)},
                subs={'a': Dir(name='a',
                               files={
                                   'f': File('f', 29116),
                                   'g': File('g', 2557),
                                   'h.lst': File('h.lst', 62596)},
                               subs={
                                   'e': Dir.of('e', [File('i', 584)], [])}),
                      'd': Dir.of(
                          name='d',
                          files=[File('j', 4060174),
                                 File('d.log', 8033020),
                                 File('d.ext', 5626152),
                                 File('k', 7214296)],
                          subdir_names=[])}),
            tree)

    def test_example_size_of_dir_e(self):
        tree = main.parse_tree(EXAMPLE)
        self.assertEqual(584, tree.subs['a'].subs['e'].calc_total_size())

    def test_example_size_of_dir_a(self):
        tree = main.parse_tree(EXAMPLE)
        self.assertEqual(94853, tree.subs['a'].calc_total_size())

    def test_example_size_of_dir_d(self):
        tree = main.parse_tree(EXAMPLE)
        self.assertEqual(24933642, tree.subs['d'].calc_total_size())

    def test_example_size_of_home(self):
        tree = main.parse_tree(EXAMPLE)
        self.assertEqual(48381165, tree.calc_total_size())

    def test_flat_tree_simple(self):
        tree = Dir.of('/', [], [])
        self.assertEqual(
            [[tree]],
            main.flat_tree([], tree))

    def test_flat_tree_depth_1(self):
        tree = Dir.of('/', [], ['a'])
        self.assertEqual(
            [[tree], [tree, Dir.of('a', [], [])]],
            main.flat_tree([], tree))

    def test_flat_tree_depth_2(self):
        tree = Dir(name='/', files={}, subs={'a': Dir.of('a', [], ['u'])})
        flat = main.flat_tree([], tree)
        self.assertEqual(3, len(flat))
        self.assertEqual('/', flat[0][0].name)
        self.assertEqual('/', flat[1][0].name)
        self.assertEqual('/', flat[2][0].name)
        self.assertEqual('a', flat[1][1].name)
        self.assertEqual('a', flat[2][1].name)
        self.assertEqual('u', flat[2][2].name)

    def test_flat_tree_from_example(self):
        tree = main.parse_tree(EXAMPLE)
        flat = main.flat_tree([], tree)
        self.assertEqual(4, len(flat))

    def test_example(self):
        tree = main.parse_tree(EXAMPLE)
        self.assertEqual((95437, 24933642), main.solve(tree))
