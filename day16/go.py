#!/usr/bin/python3

import sys

def parse(s, pos):
    ops = []
    version = int(s[pos:pos+3], 2)
    type = int(s[pos+3:pos+6], 2)
    #print('version = {}, type = {}'.format(version, type))
    pos += 6 # past version and type
    if type == 4: # literal value
        number = ''
        done = False
        while not done:
            done = int(s[pos]) == 0
            number = number + s[pos+1:pos+5]
            pos += 5
            #print('s is {}, done is {}, number is {}'.format(s[pos:], done, number))
        number = int(number, 2)
        #print('literal number is {}'.format(number))
        ops.append(number)
    else: # operator packet
        lengthtype = int(s[pos])
        pos += 1
        if lengthtype == 0: # bit length
            bitlength = int(s[pos:pos+15], 2)
            pos += 15
            #print('s is {}, bitlength is {}'.format(s[pos:], bitlength))
            delta = 0
            while delta < bitlength:
                np, op = parse(s, pos)
                ops.append(op)
                delta += np - pos
                pos = np
        else: # number of packets
            numpackets = int(s[pos:pos+11], 2)
            pos += 11
            #print('s is {}, num packets is {}'.format(s[pos:], numpackets))
            for p in range(numpackets):
                pos, op = parse(s, pos)
                ops.append(op)
    return (pos, [version, type, ops])

def sumversions(ops):
    #print('evaluating op version {}, type {}, ops {}'.format(ops[0], ops[1], ops[2]))
    sum = ops[0]
    if ops[1] != 4:
        for op in ops[2]:
            sum += sumversions(op)
    return sum

def evaluate(ops):
    #print('evaluating op version {}, type {}, ops {}'.format(ops[0], ops[1], ops[2]))
    if ops[1] == 4: # literal
        return ops[2][0]
    elif ops[1] == 0: # sum
        return sum([evaluate(op) for op in ops[2]])
    elif ops[1] == 1: # product
        product = 1
        for op in ops[2]:
            product *= evaluate(op)
        return product
    elif ops[1] == 2: # min
        return min([evaluate(op) for op in ops[2]])
    elif ops[1] == 3: # max
        return max([evaluate(op) for op in ops[2]])
    elif ops[1] == 5: # gt
        return 1 if evaluate(ops[2][0]) > evaluate(ops[2][1]) else 0
    elif ops[1] == 6: # lt
        return 1 if evaluate(ops[2][0]) < evaluate(ops[2][1]) else 0
    elif ops[1] == 7: # eq
        return 1 if evaluate(ops[2][0]) == evaluate(ops[2][1]) else 0
    else:
        print('unknown op {}'.format(ops[1]))
    return 0

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        line = f.readline().strip()

    s = ''
    for c in line:
        s += bin(int(c, 16))[2:].zfill(4)

    #print('got binary string {}'.format(s))
    pos, ops = parse(s, 0)
    #print('ops is {}'.format(ops))

    print('sum of versions is {}'.format(sumversions(ops)))
    print('evaluated to {}'.format(evaluate(ops)))
