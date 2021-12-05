#!/usr/bin/python3

import sys

def checkRow(line):
    return not line or line.count(line[0]) == len(line)

def checkWin(board):
    for i in range(5):
        if checkRow(board[i*5:i*5+5]):
            return True
    for i in range(5):
        if checkRow(board[i:i+21:5]):
            return True
    return False

if __name__ == "__main__":
    boards = []
    with open(sys.argv[1]) as f:
        numbers = f.readline().strip().split(',')
        while True:
            blank = f.readline()
            if blank == '':
                break
            boards.append(f.readline().strip().split())
            for i in range(4):
                boards[-1].extend(f.readline().strip().split())

    #print('numbers is {}'.format(numbers))
    #print('boards are {}'.format(boards))

    score = 0
    for number in numbers:
        if score != 0:
            break
        for board in boards:
            board[:] = ['X' if x == number else x for x in board]
        for board in boards.copy():
            if checkWin(board):
                print('found a winner at number {}!'.format(number))
                #print('winning board is {}'.format(board))
                score = sum([int(x) if x != 'X' else 0 for x in board])
                score *= int(number)
                break

    print('first winning score is {}'.format(score))

    score = 0
    for number in numbers:
        if score != 0:
            break
        for board in boards:
            board[:] = ['X' if x == number else x for x in board]
        for board in boards.copy():
            if checkWin(board):
                if len(boards) == 1:
                    print('found the last winner at number {}!'.format(number))
                    #print('winning board is {}'.format(board))
                    score = sum([int(x) if x != 'X' else 0 for x in board])
                    score *= int(number)
                    break
                else:
                    boards.remove(board)

    print('last winning score is {}'.format(score))
