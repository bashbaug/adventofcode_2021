#!/usr/bin/python3

import sys

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        coords = [int(x) for x in f.readline().strip().split(',')]

    #print('initial coordinates: {}'.format(coords))

    s = min(coords)
    l = max(coords)

    mincost = sys.maxsize
    for position in range(s, l):
        cost = sum([abs(x - position) for x in coords])
        if cost < mincost:
            mincost = cost
            minpos = position

    print('with simple fuel costs: smallest cost is {} at position {}'.format(mincost, minpos))

    costs = [sum(range(cost + 1)) for cost in range(l - s + 1)]

    #print('fuel costs is {}'.format(costs))

    mincost = sys.maxsize
    for position in range(s, l):
        cost = sum([costs[abs(x - position)] for x in coords])
        if cost < mincost:
            mincost = cost
            minpos = position

    print('with complex fuel costs: smallest cost is {} at position {}'.format(mincost, minpos))
