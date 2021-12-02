#!/usr/bin/python3

import sys

if __name__ == "__main__":
    values = []
    with open(sys.argv[1]) as f:
        for line in f:
            values.append(int(line))

    previous = sys.maxsize
    increases = 0
    for v in values:
        if v > previous:
            increases = increases + 1
        previous = v

    print('number of increases = {}'.format(increases))
    previous = sys.maxsize
    increases = 0

    for i, v in enumerate(values[2:]):
        sum = v + values[i+1] + values[i]
        if sum > previous:
            increases = increases + 1
        previous = sum

    print('number of increases = {}'.format(increases))
