#!/usr/bin/python3

import sys

def isOpener(c):
    return c in ['(', '[', '{', '<']

def isCloser(c):
    return c in [')', ']', '}', '>']

def getMatch(c):
    matches = {'(':')', '[':']', '{':'}', '<':'>'}
    return matches[c]

def getScore(c):
    scores = {')':3, ']':57, '}':1197, '>':25137}
    return scores[c]

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
    scores = {'(':1, '[':2, '{':3, '<':4}
    score = 0
    for c in line[::-1]:
        score = score * 5 + scores[c]
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
