#!/usr/bin/python3

import sys
import re
import copy

def intersects(a, b):
    for coord in (0, 1, 2):
        if a['min'][coord] > b['max'][coord]:
            return False
        if b['min'][coord] > a['max'][coord]:
            return False
    return True

def splitcube(s, r):
    splits = [s]
    for coord in (0, 1, 2):
        newsplits = []
        for s in splits:
            if s['min'][coord] < r['min'][coord]:
                if s['max'][coord] <= r['max'][coord]:
                    nl = copy.deepcopy(s)
                    nl['max'][coord] = r['min'][coord] - 1
                    nr = copy.deepcopy(s)
                    nr['min'][coord] = r['min'][coord]
                    newsplits.extend([nl, nr])
                else:
                    nl = copy.deepcopy(s)
                    nl['max'][coord] = r['min'][coord] - 1
                    nc = copy.deepcopy(s)
                    nc['min'][coord] = r['min'][coord]
                    nc['max'][coord] = r['max'][coord]
                    nr = copy.deepcopy(s)
                    nr['min'][coord] = r['max'][coord] + 1
                    newsplits.extend([nl, nc, nr])
            else:
                if s['max'][coord] <= r['max'][coord]:
                    newsplits.append(s)
                else:
                    nl = copy.deepcopy(s)
                    nl['max'][coord] = r['max'][coord]
                    nr = copy.deepcopy(s)
                    nr['min'][coord] = r['max'][coord] + 1
                    newsplits.extend([nl, nr])
        splits = newsplits
    return splits

def findAllCubes(lines, skipfifty=False):
    state = []
    for line in lines:
        t = re.search('^(\w+) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)', line)
        command = t.group(1)

        c = {'min': [int(t.group(2)), int(t.group(4)), int(t.group(6))],
             'max': [int(t.group(3)), int(t.group(5)), int(t.group(7))]}

        if skipfifty and \
            (c['min'][0] < -50 or c['min'][1] < -50 or c['min'][2] < -50 or \
             c['max'][0] > 50 or c['max'][1] > 50 or c['max'][2] > 50):
            print('skipping cube {}...')
            continue

        if command == 'on':
            print('+++ turning ON cube {}, state size is {}'.format(c, len(state)))
            current = [c]
            for s in state:
                newCurrent = []
                for c in current:
                    if intersects(c, s):
                        newCurrent.extend(splitcube(c, s))
                    else:
                        newCurrent.append(c)
                current = newCurrent
            for c in current:
                found = False
                for s in state:
                    if intersects(c, s):
                        found = True
                        break
                if not found:
                    state.append(c)
        elif command == 'off':
            print('--- turning OFF cube {}, state size is {}'.format(c, len(state)))
            newState = []
            for s in state:
                if intersects(c, s):
                    newState.extend(splitcube(s, c))
                else:
                    newState.append(s)
            state = []
            for s in newState:
                if not intersects(c, s):
                    state.append(s)

    count = 0
    for s in state:
        dims = [s['max'][coord] - s['min'][coord] + 1 for coord in (0, 1, 2)]
        count += dims[0] * dims[1] * dims[2]

    print('found {} cubes'.format(count))

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    findAllCubes(lines, True)
    findAllCubes(lines)
