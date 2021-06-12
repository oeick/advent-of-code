import typing
from enum import Enum
from typing import Optional

SPELLCOST = [53, 73, 113, 173, 229]


class Stats(typing.NamedTuple):
    boss_hp: int
    boss_damage: int
    player_hp: int
    player_mana: int


class Round(typing.NamedTuple):
    stats: Stats
    active_spells: list[tuple[int, int]]


class Winner(Enum):
    NO_ONE = 0
    PLAYER = 1
    BOSS = 2


class Result:
    winner: Winner
    mana: int
    next_round: Round

    def __init__(self, winner: Winner,
                 mana: Optional[int] = None,
                 next_round: Optional[Round] = None):
        self.winner = winner
        self.mana = mana
        self.next_round = next_round


def apply_active_effects(spells) -> (int, int, int, list):
    player_armor = 0
    boss_hp_delta = 0
    player_mana_delta = 0
    for spell_id, duration in spells:
        if spell_id == 2:
            if duration > 1:
                player_armor = 7
        elif spell_id == 3:
            boss_hp_delta = -3
        elif spell_id == 4:
            player_mana_delta = 101
    next_spells = [(i, d - 1) for i, d in spells if d > 1]
    return player_armor, boss_hp_delta, player_mana_delta, next_spells


def calc_next_round(
        current_round: Round,
        spell: int,
        hard: bool) -> Result:
    player_hp = current_round.stats.player_hp
    player_mana = current_round.stats.player_mana
    boss_hp = current_round.stats.boss_hp
    boss_damage = current_round.stats.boss_damage

    # *********************
    # **** Player turn ****
    # *********************

    if hard:
        player_hp -= 1
        if player_hp <= 0:
            return Result(Winner.BOSS)

    player_armor, boss_hp_delta, player_mana_delta, next_spells = \
        apply_active_effects(current_round.active_spells)
    boss_hp += boss_hp_delta
    player_mana += player_mana_delta

    if boss_hp <= 0:
        return Result(Winner.PLAYER, mana=player_mana)

    player_mana -= SPELLCOST[spell]
    if spell == 0:
        boss_hp -= 4
    elif spell == 1:
        boss_hp -= 2
        player_hp += 2
    elif spell == 2:
        next_spells.append((spell, 6))
    elif spell == 3:
        next_spells.append((spell, 6))
    elif spell == 4:
        next_spells.append((spell, 5))

    if boss_hp <= 0:
        return Result(Winner.PLAYER, mana=player_mana)

    # *******************
    # **** Boss turn ****
    # *******************

    player_armor, boss_hp_delta, player_mana_delta, next_spells = \
        apply_active_effects(next_spells)
    boss_hp += boss_hp_delta
    player_mana += player_mana_delta

    if boss_hp <= 0:
        return Result(Winner.PLAYER, mana=player_mana)

    player_hp -= max(1, boss_damage - player_armor)

    if player_hp <= 0:
        return Result(Winner.BOSS)

    return Result(
        Winner.NO_ONE,
        next_round=Round(
            stats=Stats(
                boss_hp=boss_hp,
                boss_damage=boss_damage,
                player_hp=player_hp,
                player_mana=player_mana
            ),
            active_spells=next_spells,
        )
    )


def solve(stats: Stats, hard: bool) -> int:
    current_round = Round(
        stats=stats,
        active_spells=[]
    )
    current_spell = 0
    rounds = []
    solutions = []
    best_solution = None
    spend = 0
    while True:
        rounds.append((current_round, current_spell))
        spend += SPELLCOST[current_spell]
        result = calc_next_round(current_round, current_spell, hard)
        winner = result.winner

        if winner == Winner.NO_ONE:
            if result.next_round.stats.player_mana < SPELLCOST[0]:
                winner = Winner.BOSS
            else:
                current_round = result.next_round
                current_spell = 0

        if winner == Winner.PLAYER:
            if best_solution is None or spend < best_solution[0]:
                best_solution = (spend, rounds)
            solutions.append((spend, rounds))
            winner = Winner.BOSS

        if winner == Winner.BOSS:
            go_back = True
            while True:
                if go_back:
                    if len(rounds) == 0:
                        return best_solution[0]
                    current_round, current_spell = rounds.pop()
                    spend -= SPELLCOST[current_spell]
                    go_back = False
                current_spell += 1
                if current_spell > 4:
                    go_back = True
                elif SPELLCOST[current_spell] > current_round.stats.player_mana:
                    go_back = True
                elif best_solution and \
                        spend + SPELLCOST[current_spell] > best_solution[0]:
                    go_back = True
                elif current_spell not in \
                        [s for s, d in current_round.active_spells if d > 1]:
                    break


def main(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    stats = Stats(boss_hp=int(lines[0].split(':')[1]),
                  boss_damage=int(lines[1].split(':')[1]),
                  player_hp=50,
                  player_mana=500, )
    return (solve(stats, hard=False),
            solve(stats, hard=True))


if __name__ == '__main__':
    solution_1, solution_2 = main('../input.txt')
    print(solution_1, solution_2)
