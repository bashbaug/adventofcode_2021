#!/usr/bin/python3

import sys

if __name__ == "__main__":
    lines = []
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    gamma = 0
    epsilon = 0

    for bit in range(0, len(lines[0].strip())):
        ones = sum([1 if line[bit] == '1' else 0 for line in lines])
        gamma = gamma * 2 + (1 if ones > len(lines) / 2 else 0)
        epsilon = epsilon * 2 + (1 if ones < len(lines) / 2 else 0)

    print('gamma is {}, epsilon is {}, power is {}'.format(gamma, epsilon, gamma * epsilon))

    orig = lines.copy()

    for bit in range(0, len(lines[0].strip())):
        if len(lines) == 1:
            break
        ones = sum([1 if line[bit] == '1' else 0 for line in lines])
        if ones >= len(lines) / 2:
            for i in range(len(lines)-1, -1, -1):
                if lines[i][bit] == '0':
                    lines.remove(lines[i])
        else:
            for i in range(len(lines)-1, -1, -1):
                if lines[i][bit] == '1':
                    lines.remove(lines[i])

    oxy = lines[0].strip()
    print('oxygen generator rating = {} = {}'.format(oxy, int(oxy, 2)))

    lines = orig.copy()

    for bit in range(0, len(lines[0].strip())):
        if len(lines) == 1:
            break
        ones = sum([1 if line[bit] == '1' else 0 for line in lines])
        if ones < len(lines) / 2:
            for i in range(len(lines)-1, -1, -1):
                if lines[i][bit] == '0':
                    lines.remove(lines[i])
        else:
            for i in range(len(lines)-1, -1, -1):
                if lines[i][bit] == '1':
                    lines.remove(lines[i])

    c02 = lines[0].strip()
    print('c02 scrubber rating = {} = {}'.format(c02, int(c02, 2)))

    lsr = int(oxy, 2) * int(c02, 2)
    print('life support rating = {}'.format(lsr))
