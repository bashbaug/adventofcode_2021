#!/usr/bin/python3

import sys

def update(state, r, c):
    if r >= 0 and r < len(state):
        if c >= 0 and c < len(state[r]):
            state[r][c] += 1
            if state[r][c] == 10:
                update(state, r-1, c-1)
                update(state, r  , c-1)
                update(state, r+1, c-1)
                update(state, r-1, c  )
                update(state, r+1, c  )
                update(state, r-1, c+1)
                update(state, r  , c+1)
                update(state, r+1, c+1)

def flash(state):
    flashes = 0
    for r, row in enumerate(state):
        for c, s in enumerate(row):
            if state[r][c] > 9:
                flashes += 1
                state[r][c] = 0
    return flashes

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    state = [[int(c) for c in line.strip()] for line in lines]

    flashes = 0
    step = 0
    doneA = False
    doneB = False
    while not doneA or not doneB:
        step = step + 1
        for r, row in enumerate(state):
            for c, s in enumerate(row):
                update(state, r, c)
        count = flash(state)
        flashes += count
        if step == 100:
            print('after step {}, flashes is {}'.format(step, flashes))
            doneA = True
        if count == 100:
            print('on step {} all flashed'.format(step))
            doneB = True
