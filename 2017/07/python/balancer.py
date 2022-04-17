from collections import Counter
from typing import Optional

from program import Program

PSEUDO_INFINITY = 2 ** 32


class Balancer:
    programs: dict[str, Program]

    def __init__(self, programs: dict[str, Program]):
        self.programs = programs

    def balance_weight(self) -> int:
        new_weight = PSEUDO_INFINITY
        for progr in self.programs.values():
            if progr.subs:
                if adjusted := self._balance_sub_weight(progr.subs):
                    new_weight = min(adjusted, new_weight)
        return new_weight

    def _calc_total_weight(self, program: str) -> int:
        weight = self.programs[program].weight
        subs = self.programs[program].subs
        if subs:
            weight += sum([self._calc_total_weight(p) for p in subs])
        return weight

    def _balance_sub_weight(self, subs: list[str]) -> Optional[int]:
        sub_weights = {s: self._calc_total_weight(s) for s in subs}
        counts = Counter(sub_weights.values()).most_common()
        if len(counts) > 1:
            right_weight, wrong_weight = counts[0][0], counts[-1][0]
            sub = next(s for s, w in sub_weights.items() if w == wrong_weight)
            return self.programs[sub].weight + right_weight - wrong_weight
