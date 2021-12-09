#!/usr/bin/python3

import sys

def makeInt(s):
    result = 0
    result |= (1 << 6) if s.find('a') >= 0 else 0
    result |= (1 << 5) if s.find('b') >= 0 else 0
    result |= (1 << 4) if s.find('c') >= 0 else 0
    result |= (1 << 3) if s.find('d') >= 0 else 0
    result |= (1 << 2) if s.find('e') >= 0 else 0
    result |= (1 << 1) if s.find('f') >= 0 else 0
    result |= (1 << 0) if s.find('g') >= 0 else 0
    return result

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = [x.strip().split(' | ') for x in f.readlines()]

    counts = [0 for x in range(10)]
    for x, output in lines:
        for digit in output.split():
            counts[1] += 1 if len(digit) == 2 else 0
            counts[4] += 1 if len(digit) == 4 else 0
            counts[7] += 1 if len(digit) == 3 else 0
            counts[8] += 1 if len(digit) == 7 else 0

    print('number of instances is {}'.format(sum(counts)))

    sum = 0
    for d, o in lines:
        digits = [makeInt(s) for s in d.split()]
        output = [makeInt(s) for s in o.split()]
        #print('digits are {}, output is {}'.format(
        #    [format(i, '07b') for i in digits],
        #    [format(i, '07b') for i in output]))
        decoded = [0 for x in range(10)]
        decoded[1] = [x for x in digits if bin(x).count("1") == 2][0]
        decoded[4] = [x for x in digits if bin(x).count("1") == 4][0]
        decoded[7] = [x for x in digits if bin(x).count("1") == 3][0]
        decoded[8] = [x for x in digits if bin(x).count("1") == 7][0]

        decoded[3] = [x for x in digits if bin(x).count("1") == 5 and x & decoded[1] == decoded[1]][0]
        decoded[6] = [x for x in digits if bin(x).count("1") == 6 and x & decoded[1] != decoded[1]][0]

        decoded[5] = [x for x in digits if bin(x).count("1") == 5 and x & decoded[6] == x][0]
        decoded[2] = [x for x in digits if bin(x).count("1") == 5 and x != decoded[3] and x != decoded[5]][0]

        decoded[9] = [x for x in digits if bin(x).count("1") == 6 and x != decoded[6] and x & decoded[5] == decoded[5]][0]
        decoded[0] = [x for x in digits if bin(x).count("1") == 6 and x != decoded[6] and x != decoded[9]][0]

        #print('decoded {}'.format(
        #    [format(i, '07b') for i in decoded]))

        result = 0
        for x in output:
            result *= 10
            result += [i for i, d in enumerate(decoded) if d == x][0]

        #print('result is {}'.format(result))
        sum += result

    print('sum of results is {}'.format(sum))
