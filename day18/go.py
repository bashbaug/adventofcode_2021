#!/usr/bin/python3

import sys
import ast
import copy

def incrementchild(sl, child, value):
    if type(sl[child]) is list:
        sl = sl[child]
        while type(sl[1-child]) is list:
            sl = sl[1-child]
        sl[1-child] += value
    else:
        sl[child] += value

def explode(sl, depth):
    done = False
    l, r = -1, -1
    if not done:
        if type(sl[0]) is list:
            if depth == 4:
                l, r = sl[0][0], sl[0][1]
                incrementchild(sl, 1, r)
                sl[0] = 0
                return True, l, -1
            else:
                done, l, r = explode(sl[0], depth + 1)
                if done and r >= 0:
                    incrementchild(sl, 1, r)
                    r = -1
    if not done:
        if type(sl[1]) is list:
            if depth == 4:
                l, r = sl[1][0], sl[1][1]
                incrementchild(sl, 0, l)
                sl[1] = 0
                return True, -1, r
            else:
                done, l, r = explode(sl[1], depth + 1)
                if done and l >= 0:
                    incrementchild(sl, 0, l)
                    l = -1
    return done, l, r

def split(sl):
    done = False
    if type(sl[0]) is list:
        done = split(sl[0])
    elif sl[0] >= 10:
        sl[0] = [sl[0] // 2, (sl[0] + 1) // 2]
        done = True
    if not done:
        if type(sl[1]) is list:
            done = split(sl[1])
        elif sl[1] >= 10:
            sl[1] = [sl[1] // 2, (sl[1] + 1) // 2]
            done = True
    return done

def reduce(sl):
    while True:
        done, x, x = explode(sl, 1)
        if done:
            #print('after explode:  {}'.format(sl))
            continue
        if split(sl):
            #print('after split:    {}'.format(sl))
            continue
        break

def magnitude(sl):
    if type(sl) is list:
        return 3 * magnitude(sl[0]) + 2 * magnitude(sl[1])
    else:
        return sl

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    ops = [ast.literal_eval(x.strip()) for x in lines]

    sl = copy.deepcopy(ops[0])
    for op in ops[1:]:
        sl = [sl, copy.deepcopy(op)]
        reduce(sl)

    print('final sum is {}'.format(sl))
    print('magnitude is {}'.format(magnitude(sl)))

    m = 0
    for i, op0 in enumerate(ops):
        for j, op1 in enumerate(ops):
            if i != j:
                sl = [copy.deepcopy(op0), copy.deepcopy(op1)]
                reduce(sl)
                m = max(m, magnitude(sl))
    
    print('maximum magnitude is {}'.format(m))
