import random
from typing import Union

from piglr.state import State, as_dict
from piglr.error import IllegalParameterError


class Game:
    def __init__(self, players: int = 2, num_dice: int = 1, dn: int = 6, target: int = 100):
        for param in [players, num_dice, dn, target]:
            if not isinstance(param, int):
                param_name = f'{param=}'.split('=')[0]
                raise TypeError(f'Param {param_name} must be of type int')

        if players < 2:
            raise IllegalParameterError('There must be at least 2 players')

        if num_dice < 1:
            raise IllegalParameterError('There must be at least 1 dice')

        if dn < 2:
            raise IllegalParameterError('The dice must be at least 2 sided')

        if target < 1:
            raise IllegalParameterError('The target must be positive')

        self.players = players
        self.num_dice = num_dice
        self.dn = dn
        self.target = target

    @property
    def state(self) -> dict:
        return as_dict(self._state)

    def _increment_turn(self, bank: bool) -> None:
        if bank:
            self._state.score[self._state.turn] += self._state.bank

        self._state.rolls = 0
        self._state.bank = 0

        if self._state.players - 1 == self._state.turn:
            self._state.turn = 0
        else:
            self._state.turn += 1

    def _check_for_winner(self) -> Union[int, None]:
        if max(self._state.score.values()) >= self._state.target:
            return max(self._state.score, key=self._state.score.get)
        return None

    def reset(self) -> Union[dict, None]:
        self._state = State(
            players=self.players,
            num_dice=self.num_dice,
            dn=self.dn,
            score={i:0 for i in range(self.players)},
            target=self.target
        )

        return self.state, None

    def roll(self) -> Union[dict, None]:
        d = random.randint(1, self._state.dn)
        if d == 1:
            self._increment_turn(bank=False)
        else:
            self._state.rolls += 1
            self._state.bank += d

        return self.state, None
    
    def bank(self) -> Union[dict, Union[int, None]]:
        self._increment_turn(bank=True)

        winner = self._check_for_winner()

        return self.state, winner
