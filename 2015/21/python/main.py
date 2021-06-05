import copy
import itertools
import math
import typing


class Stats(typing.NamedTuple):
    hp: int
    damage: int
    armor: int


class Item(typing.NamedTuple):
    cost: int = 0
    damage: int = 0
    armor: int = 0


SHOP_INVENTORY = {
    'Weapons': {
        'Dagger': Item(cost=8, damage=4),
        'Shortsword': Item(cost=10, damage=5),
        'Warhammer': Item(cost=25, damage=6),
        'Longsword': Item(cost=40, damage=7),
        'Greataxe': Item(cost=74, damage=8),
    },
    'Armor': {
        'No': Item(),
        'Leather': Item(cost=13, armor=1),
        'Chainmail': Item(cost=31, armor=2),
        'Splintmail': Item(cost=53, armor=3),
        'Bandedmail': Item(cost=75, armor=4),
        'Platemail': Item(cost=102, armor=5),
    },
    'Rings': {
        'No': Item(),
        'Damage +1': Item(cost=25, damage=1),
        'Damage +2': Item(cost=50, damage=2),
        'Damage +3': Item(cost=100, damage=3),
        'Defense +1': Item(cost=20, armor=1),
        'Defense +2': Item(cost=40, armor=2),
        'Defense +3': Item(cost=80, armor=3),
    }
}


class Shop:
    inventory: dict

    def __init__(self, inventory):
        self.inventory = copy.deepcopy(inventory)

    def buy_next(self) -> (set, int):
        item_sets = itertools.product(
            self.inventory['Weapons'].values(),
            self.inventory['Armor'].values(),
            self.inventory['Rings'].values(),
            self.inventory['Rings'].values()
        )
        for item_set in item_sets:
            if item_set[2] == item_set[3] and not item_set[2] == Item():
                continue
            yield set(item_set), sum(i.cost for i in item_set)


def calculate_player_stats(items: set) -> Stats:
    return Stats(
        damage=sum(i.damage for i in items),
        armor=sum(i.armor for i in items),
        hp=100)


def fight(player: Stats, boss: Stats) -> bool:
    """ Returns `True` when player wins, `False` otherwise. """
    player_damage = max(1, player.damage - boss.armor)
    boss_damage = max(1, boss.damage - player.armor)
    rounds_to_boss_death = math.ceil(boss.hp / player_damage)
    rounds_to_player_death = math.ceil(player.hp / boss_damage)
    return rounds_to_boss_death <= rounds_to_player_death


def solve(boss_stats: Stats) -> (int, int):
    least_amount = 999
    most_amount = 0
    shop = Shop(SHOP_INVENTORY)
    for items, cost in shop.buy_next():
        player_stats = calculate_player_stats(items)
        win = fight(player_stats, boss_stats)
        if win:
            least_amount = min(least_amount, cost)
        else:
            most_amount = max(most_amount, cost)
    return least_amount, most_amount


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    boss_stats = Stats(
        hp=int(lines[0].split(':')[1]),
        damage=int(lines[1].split(':')[1]),
        armor=int(lines[2].split(':')[1]),
    )
    return solve(boss_stats)


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1)
    print(solution_2)
