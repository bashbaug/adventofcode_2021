#!/usr/bin/python3

import sys
import re

def findheight(velocity, target):
    position = [0, 0]
    maxheight = 0
    #print('position = {}, velocity = {}'.format(position, velocity))
    while True:
        position[0] += velocity[0]
        position[1] += velocity[1]
        maxheight = max(maxheight, position[1])

        velocity[0] += -1 if velocity[0] > 0 else 1 if velocity[0] < 0 else 0
        velocity[1] += -1

        #print('position = {}, velocity = {}'.format(position, velocity))

        if position[0] >= target[0][0] and \
           position[0] <= target[0][1] and \
           position[1] >= target[1][0] and \
           position[1] <= target[1][1]:
            return (True, maxheight)
        if position[0] > target[0][1]:
            return (False, 0)
        if position[1] < target[1][0]:
            return (False, 0)
        if velocity[0] == 0 and position[0] < target[0][0]:
            #print('early exit: velocity is {}, position is {}, target is {}'.format(velocity[0], position[0], target[0][0]))
            return (False, 0)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        line = f.readline()

    t = re.search('^target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)', line)

    target = [[int(t.group(1)), int(t.group(2))], [int(t.group(3)), int(t.group(4))]]

    print('got target = {}'.format(target))

    maxheight = 0
    count = 0
    for vx in range(500):
        for vy in range(-500, 500):
            found, height = findheight([vx, vy], target)
            #print('velocity is {}: found {}: height is {}'.format([vx, vy], found, height))
            maxheight = max(maxheight, height) if found else maxheight
            count = count + (1 if found else 0)

    print('found maximum height {}'.format(maxheight))
    print('found {} velocity values'.format(count))
