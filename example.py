import json
import random

import piglr


if __name__ == '__main__':
    game = piglr.Game()

    obs, winner = game.reset()
    while winner is None:
        roll = random.randint(0, 1)
        if roll:
            obs, winner = game.roll()
        else:
            obs, winner = game.bank()

    print(json.dumps(obs, indent=4))
    print(f'Winner: {winner}')
