#!/usr/bin/python3

import sys

def update(risks, costs, visited, working, current, x, y):
    if y >= 0 and y < len(costs) and x >= 0 and x < len(costs[y]) and not visited[y][x]:
        cost = current + risks[y][x]
        costs[y][x] = min(costs[y][x], cost)
        working[(y, x)] = costs[y][x]

def findminpath(risks):
    costs = [[sys.maxsize for i in row] for row in risks]
    visited = [[False for i in row] for row in risks]

    working = {}
    costs[0][0] = 0
    working[(0, 0)] = 0
    while len(working) != 0:
        #print('working len is {}, is now: {}'.format(len(working), working))
        y, x = min(working, key = working.get)
        del working[(y, x)]
        #print('evaluating y = {}, x = {}'.format(y, x))
        visited[y][x] = True

        update(risks, costs, visited, working, costs[y][x], x  , y-1)
        update(risks, costs, visited, working, costs[y][x], x-1, y  )
        update(risks, costs, visited, working, costs[y][x], x+1, y  )
        update(risks, costs, visited, working, costs[y][x], x  , y+1)

    #print('costs is:')
    #print(*costs, sep='\n')
    return costs[-1][-1]


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    risks = [[int(c) for c in line.strip()] for line in lines]
    print('risks is {} rows x {} cols'.format(len(risks), len(risks[0])))
    #print(*risks, sep='\n')

    print('lowest risk path has cost {}'.format(findminpath(risks)))

    newrisks = []
    for risk in risks:
        newrisk = []
        for i in range(5):
            for x in risk:
                v = x + i
                v = v if v <= 9 else v - 9
                newrisk.append(v)
        newrisks.append(newrisk)
    risks = newrisks.copy()
    #print('horizontal expansion is {} rows x {} cols:'.format(len(risks), len(risks[0])))
    #print(*risks, sep='\n')
    newrisks = []
    for i in range (5):
        for risk in risks:
            newrisk = []
            for x in risk:
                v = x + i
                v = v if v <= 9 else v - 9
                newrisk.append(v)
            newrisks.append(newrisk)
    print('newrisks is {} rows x {} cols'.format(len(newrisks), len(newrisks[0])))
    #print(*newrisks, sep='\n')
    risks = newrisks.copy()

    print('lowest risk path has cost {}'.format(findminpath(risks)))
