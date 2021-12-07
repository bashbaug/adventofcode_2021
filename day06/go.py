#!/usr/bin/python3

import sys

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        state = [int(x) for x in f.readline().strip().split(',')]

    #print('Initial state: {}'.format(state))

    counts = [state.count(i) for i in range(9)]

    #print('counts: {}'.format(counts))

    for day in range(256):
        cycle = counts[0]
        counts[:-1] = counts[1:]
        counts[6] += cycle
        counts[8] = cycle

        #for i in range(len(state)):
        #    if state[i] == 0:
        #        state[i] = 6
        #        state.append(8)
        #    else:
        #        state[i] -= 1
        #print('counts: {}'.format(counts))
        #print(' check: {}'.format([state.count(i) for i in range(9)]))
        #print('bruteforce: after {} days there are {} fish'.format(day + 1, len(state)))
        print('    clever: after {} days there are {} fish'.format(day + 1, sum(counts)))
