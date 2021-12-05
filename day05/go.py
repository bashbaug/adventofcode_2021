#!/usr/bin/python3

import sys

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        coords = [x.strip().split(' -> ') for x in f.readlines()]

    maxx = 0
    maxy = 0
    for coord in coords:
        s = [int(x) for x in coord[0].split(',')]
        e = [int(x) for x in coord[1].split(',')]
        #print('s is {}, e is {}'.format(s, e))
        maxx = max(maxx, s[0], e[0])
        maxy = max(maxy, s[1], e[1])

    #print('maxx is {}, maxy is {}'.format(maxx, maxy))

    board = [[0 for x in range(maxx + 1)] for y in range(maxy + 1)]
    #print('initial board is {}'.format(board))
    for coord in coords:
        c0 = [int(x) for x in coord[0].split(',')]
        c1 = [int(x) for x in coord[1].split(',')]
        s = min(c0, c1)
        e = max(c0, c1)
        #print('s is {}, e is {}'.format(s, e))
        if s[0] == e[0]:
            x = s[0]
            for y in range(s[1], e[1] + 1): board[y][x] += 1
        elif s[1] == e[1]:
            y = s[1]
            for x in range(s[0], e[0] + 1): board[y][x] += 1
        #print(*board, sep='\n')

    count = sum([1 if x > 1 else 0 for col in board for x in col])
    print('without diagonals, count is {}'.format(count))

    for coord in coords:
        c0 = [int(x) for x in coord[0].split(',')]
        c1 = [int(x) for x in coord[1].split(',')]
        s = min(c0, c1)
        e = max(c0, c1)
        #print('s is {}, e is {}'.format(s, e))
        if s[0] != e[0] and s[1] < e[1]:
            x = s[0]
            y = s[1]
            for i in range(e[0] - s[0] + 1): board[y + i][x + i] += 1
        elif s[0] != e[0] and s[1] > e[1]:
            x = s[0]
            y = s[1]
            for i in range(e[0] - s[0] + 1): board[y - i][x + i] += 1
        #print(*board, sep='\n')

    count = sum([1 if x > 1 else 0 for col in board for x in col])
    print('with diagonals, count is {}'.format(count))
