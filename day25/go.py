#!/usr/bin/python3

import sys

def wrap(state, coord):
    nr, nc = coord
    if nr >= len(state):
        nr = 0
    if nc >= len(state[nr]):
        nc = 0
    return (nr, nc)

def stepright(state):
    newstate = [['.' for i in range(len(row))] for row in state]
    moves = 0
    for r, row in enumerate(state):
        for c, s in enumerate(row):
            if s == 'v':
                newstate[r][c] = s
            elif s == '>':
                nr, nc = wrap(state, (r, c+1))
                if state[nr][nc] == '.':
                    newstate[nr][nc] = s
                    moves += 1
                else:
                    newstate[r][c] = s
    return moves, newstate

def stepdown(state):
    newstate = [['.' for i in range(len(row))] for row in state]
    moves = 0
    for r, row in enumerate(state):
        for c, s in enumerate(row):
            if s == '>':
                newstate[r][c] = s
            elif s == 'v':
                nr, nc = wrap(state, (r+1, c))
                if state[nr][nc] == '.':
                    newstate[nr][nc] = s
                    moves += 1
                else:
                    newstate[r][c] = s
    return moves, newstate

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    state = [[c for c in line.strip()] for line in lines]
    #print('initial state is:')
    #print(*state, sep='\n')

    step = 0
    while True:
        step += 1
        movesr, state = stepright(state)
        movesd, state = stepdown(state)
        #print('after step {} (moved {} right, {} down):'.format(step, movesr, movesd))
        #print(*state, sep='\n')
        if movesr + movesd == 0:
            print('there are no moves after {} steps'.format(step))
            break
