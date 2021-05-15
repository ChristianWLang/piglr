import random

import numpy as np
import pytest

import piglr


def test_init():
    game = piglr.Game(2, 1, 6, 100)
    game.reset()

    assert game.players == 2
    assert game.num_dice == 1
    assert game.dn == 6
    assert game.target == 100


def test_init_errors():
    with pytest.raises(piglr.error.IllegalParameterError):
        # Check for fewer than 2 players
        game = piglr.Game(1, 1, 6, 100)
        game.reset()
    with pytest.raises(piglr.error.IllegalParameterError):
        # Check for fewer than 1 die
        game = piglr.Game(2, 0, 6, 100)
        game.reset()
    with pytest.raises(piglr.error.IllegalParameterError):
        # Check for die with fewer than 2 sides
        game = piglr.Game(2, 1, 1, 100)
        game.reset()
    with pytest.raises(piglr.error.IllegalParameterError):
        # Check for score < 1
        game = piglr.Game(2, 1, 6, 0)
        game.reset()
