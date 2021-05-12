from dataclasses import dataclass, asdict
from typing import Dict


@dataclass
class State:
    players: int
    num_dice: int
    dn: int
    score: Dict[int, int]
    target: int
    turn: int = 0
    rolls: int = 0
    bank: int = 0


def as_dict(state: State) -> dict:
    return asdict(state)
