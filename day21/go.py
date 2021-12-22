#!/usr/bin/python3

import sys

increments = {3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1}

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    positions = [int(x) - 1 for (h, x) in (line.strip().split(':') for line in lines)]

    backup = positions.copy()

    rolls = 0
    scores = [0] * len(positions)
    done = False
    while not done:
        for player, pos in enumerate(positions):
            pos = (pos + sum([(rolls + i) % 100 + 1 for i in (0, 1, 2)])) % 10
            scores[player] += pos + 1
            positions[player] = pos
            rolls += 3
            if scores[player] >= 1000:
                print('losing score is {}, rolls is {}, product is {}'. \
                    format(scores[1-player], rolls, scores[1-player] * rolls))
                done = True
                break

    positions = backup
    universes = [{} for position in (positions)]
    wins = [0] * 2
    universes[0][(positions[0], 0)] = 1
    universes[1][(positions[1], 0)] = 1
    while True:
        if len(universes[0]) + len(universes[1]) == 0:
            break
        for player, universe in enumerate(universes):
            newuniverse = {}
            for outcome in universe:
                for inc in increments:
                    pos = (outcome[0] + inc) % 10
                    score = outcome[1] + pos + 1
                    count = universe[outcome] * increments[inc]
                    if score >= 21:
                        wins[player] += (count * sum(universes[1-player].values()))
                    else:
                        newuniverse[(pos, score)] = newuniverse.setdefault((pos, score), 0) + count
            universes[player] = newuniverse

    print('wins is {}, max wins is {}'.format(wins, max(wins)))
