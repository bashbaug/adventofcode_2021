#!/usr/bin/python3

import sys

if __name__ == "__main__":
    commands = []
    with open(sys.argv[1]) as f:
        for line in f:
            commands.append(line.split())

    pos = 0
    depth = 0
    for command in commands:
        v = int(command[1])
        if command[0] == 'forward':
            pos += v
        elif command[0] == 'up':
            depth -= v
        elif command[0] == 'down':
            depth += v

    print('part 1: position = {}, depth = {}, product = {}'.format(pos, depth, pos * depth))

    pos = 0
    depth = 0
    aim = 0
    for command in commands:
        v = int(command[1])
        if command[0] == 'forward':
            pos += v
            depth += aim * v
        elif command[0] == 'up':
            aim -= v
        elif command[0] == 'down':
            aim += v

    print('part 2: position = {}, depth = {}, product = {}'.format(pos, depth, pos * depth))
