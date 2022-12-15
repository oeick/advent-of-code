from dataclasses import dataclass
from typing import NamedTuple, Self


class File(NamedTuple):
    name: str
    size: int


@dataclass
class Dir:
    name: str
    files: dict[str, File]
    subs: dict[str, Self]

    def calc_total_size(self) -> int:
        return sum(f.size for f in self.files.values()) \
               + sum(d.calc_total_size() for d in self.subs.values())

    @staticmethod
    def of(name: str,
           files: list[File],
           subdir_names: list[str]) -> Self:
        return Dir(name=name,
                   files={f.name: f for f in files},
                   subs={s: Dir(s, {}, {}) for s in subdir_names})

    def ensure_existence_of_dir(self, sub: str) -> None:
        if sub not in self.subs:
            self.subs[sub] = Dir(sub, {}, {})

    def ensure_existence_of_file(self, name: str, size: int) -> None:
        if name not in self.files:
            self.files[name] = File(name, size)


def main(filename: str) -> tuple[int, int]:
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    tree = parse_tree(lines)
    return solve(tree)


def parse_tree(lines: list[str]) -> Dir:
    home = Dir.of('/', [], [])
    parent_dirs: list[Dir] = []
    current_dir: Dir = home
    for line in lines:
        if line.startswith('$ cd /'):
            current_dir = home
        elif line.startswith('dir '):
            current_dir.ensure_existence_of_dir(line.split()[1])
        elif line[0].isnumeric():
            current_dir.ensure_existence_of_file(
                name=line.split()[1],
                size=int(line.split()[0]))
        elif line.startswith('$ cd ..'):
            current_dir = parent_dirs.pop()
        elif line.startswith('$ cd '):
            parent_dirs.append(current_dir)
            current_dir = current_dir.subs[line.split()[-1]]
    return home


def flat_tree(pre_paths: list[Dir], current: Dir) -> list[list[Dir]]:
    flat = [pre_paths + [current]]
    for sub_dir in current.subs.values():
        flat += flat_tree(pre_paths + [current], sub_dir)
    return flat


def solve(tree: Dir) -> tuple[int, int]:
    paths = flat_tree([], tree)
    sizes = [p[-1].calc_total_size() for p in paths]
    min_size = 30_000_000 - (70_000_000 - tree.calc_total_size())
    filtered_sizes = [s for s in sizes if s >= min_size]
    return sum([s for s in sizes if s <= 100_000]), min(filtered_sizes)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
