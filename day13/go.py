#!/usr/bin/python3

import sys

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    empty = lines.index('\n')
    coords = [[int(x) for x in line.strip().split(',')] for line in lines[:empty]]
    folds = [line.strip().split('=') for line in lines[empty + 1:]]
    folds = [[x, int(y)] for [x, y] in folds]

    #print('Got coords {}'.format(coords))
    #print('Got folds {}'.format(folds))
    
    maxx = max(coords, key = lambda i : i[0])[0] + 1
    maxy = max(coords, key = lambda i : i[1])[1] + 1

    board = [[0 for x in range(maxx)] for y in range(maxy)]
    for coord in coords:
        x = coord[0]
        y = coord[1]
        board[y][x] = 1

    #print('Initial board is:')
    #print(*board, sep='\n')

    for i, fold in enumerate(folds):
        if fold[0] == 'fold along x':
            maxy = len(board)
            maxx = fold[1]
            newboard = [[0 for x in range(maxx)] for y in range(maxy)]
            for y in range(len(board)):
                for x in range(len(board[0])):
                    if board[y][x] == 1:
                        if x < maxx:
                            newboard[y][x] = 1
                        elif x > maxx:
                            newboard[y][2 * maxx - x] = 1
        if fold[0] == 'fold along y':
            maxx = len(board[0])
            maxy = fold[1]
            newboard = [[0 for x in range(maxx)] for y in range(maxy)]
            for y in range(len(board)):
                for x in range(len(board[0])):
                    if board[y][x] == 1:
                        if y < maxy:
                            newboard[y][x] = 1
                        elif y > maxy:
                            newboard[2 * maxy - y][x] = 1
        board = newboard
        if i == 0:
            print('after first fold: dots is {}'.format(sum([sum(r) for r in board])))

    print('Final board is:')
    print(*board, sep='\n')
