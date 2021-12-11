#!/usr/bin/python3

import sys

def isOpener(c):
    return c == '(' or c == '[' or c == '{' or c == '<'

def isCloser(c):
    return c == ')' or c == ']' or c == '}' or c == '>'

def getMatch(c):
    match = ')' if c == '(' else 'X'
    match = ']' if c == '[' else match
    match = '}' if c == '{' else match
    match = '>' if c == '<' else match
    return match

def getScore(c):
    res = 3 if c == ')' else 0
    res = 57 if c == ']' else res
    res = 1197 if c == '}' else res
    res = 25137 if c == '>' else res
    return res

def hasCloser(line):
    for c in line:
        if isCloser(c):
            return True
    return False

def getMinimal(line):
    while True:
        if len(line) == 0:
            return line
        if not hasCloser(line):
            return line
        for i, c in enumerate(line[:-1]):
            n = line[i+1]
            if isOpener(c) and isCloser(n):
                if n == getMatch(c):
                    line = line[:i] + line[i+2:]
                    break
                else:
                    return line
    return line

def getSyntaxErrorPoints(line):
    for c in line:
        if isCloser(c):
            return getScore(c)
    return 0

def getAutocompletePoints(line):
    score = 0
    for c in line[::-1]:
        score = score * 5
        score += 1 if c == '(' else 0
        score += 2 if c == '[' else 0
        score += 3 if c == '{' else 0
        score += 4 if c == '<' else 0
    return score

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    lines = [getMinimal(line.strip()) for line in lines]
    points = [getSyntaxErrorPoints(line) for line in lines]
    print('got syntax error points {}'.format(sum(points)))

    lines = [line for line in lines if not hasCloser(line)]
    points = [getAutocompletePoints(line) for line in lines]
    points.sort()
    print('middle autocorrect points is {}'.format(points[len(points)//2]))
