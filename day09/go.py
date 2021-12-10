#!/usr/bin/python3

import sys

def canL(board, x, y):
    return x > 0

def canR(board, x, y):
    return x < len(board[y]) - 1

def canU(board, x, y):
    return y > 0

def canB(board, x, y):
    return y < len(board) - 1

def isLowPoint(board, x, y):
    ret = (board[y][x-1] if canL(board, x, y) else 99) > board[y][x]
    ret = (board[y][x+1] if canR(board, x, y) else 99) > board[y][x] and ret
    ret = (board[y-1][x] if canU(board, x, y) else 99) > board[y][x] and ret
    ret = (board[y+1][x] if canB(board, x, y) else 99) > board[y][x] and ret
    return ret

def getBasinSize(board, x, y):
    size = 1
    board[y][x] = 9
    if canL(board, x, y) and board[y][x-1] != 9:
        size += getBasinSize(board, x-1, y)
    if canR(board, x, y) and board[y][x+1] != 9:
        size += getBasinSize(board, x+1, y)
    if canU(board, x, y) and board[y-1][x] != 9:
        size += getBasinSize(board, x, y-1)
    if canB(board, x, y) and board[y+1][x] != 9:
        size += getBasinSize(board, x, y+1)
    return size

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        board = [[int(c) for c in x.strip()] for x in f.readlines()]

    count = 0
    for y in range(len(board)):
        for x in range(len(board[y])):
            count += 1 + int(board[y][x]) if isLowPoint(board, x, y) else 0

    print('sum of risk levels is {}'.format(count))

    basins = []
    for y in range(len(board)):
        for x in range(len(board[y])):
            if isLowPoint(board, x, y):
                count = getBasinSize(board, x, y)
                basins.append(count)

    basins.sort()
    count = basins[-3] * basins[-2] * basins[-1]
    print('three biggest basins are {} product is {}'.format(basins[-3:], count))
