#!/usr/bin/python3

import sys
import copy

def expand(data, steps):
    for i in range(len(data)):
        data[i] = '.' * steps + data[i] + '.' * steps
    blank = '.' * len(data[0])
    for i in range(steps):
        data.insert(0, blank)
        data.append(blank)

def findKey(data, r, c):
    nr = len(data)
    nc = len(data[0])
    key = 0
    key += 256 if c > 0    and r > 0    and data[r-1][c-1] == '#' else 0
    key += 128 if              r > 0    and data[r-1][c  ] == '#' else 0
    key +=  64 if c < nc-1 and r > 0    and data[r-1][c+1] == '#' else 0
    key +=  32 if c > 0                 and data[r  ][c-1] == '#' else 0
    key +=  16 if                           data[r  ][c  ] == '#' else 0
    key +=   8 if c < nc-1              and data[r  ][c+1] == '#' else 0
    key +=   4 if c > 0    and r < nr-1 and data[r+1][c-1] == '#' else 0
    key +=   2 if              r < nr-1 and data[r+1][c  ] == '#' else 0
    key +=   1 if c < nc-1 and r < nr-1 and data[r+1][c+1] == '#' else 0
    return key

def enhance(keystring, data):
    newdata = copy.deepcopy(data)
    for row in range(len(data)):
        newline = ''
        for col in range(len(data[row])):
            #print('enhancing {}, {} (out of {}, {})'.format(row, col, len(data), len(data[row])))
            key = findKey(data, row, col)
            #print('at row {}, col {}: got key {} --> {}'.format(row, col, key, keystring[key]))
            newline += keystring[key]
        newdata[row] = newline
    return newdata

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    keystring = lines[0]
    data = [line.strip() for line in lines[2:]]

    #print('got key string:')
    #print(keystring)
    #print('got image data {}: rows x {} cols:'.format(len(data), len(data[0])))
    #print(*data, sep='\n')

    steps = 50
    expand(data, steps * 2)

    #print('expanded image data {}: rows x {} cols:'.format(len(data), len(data[0])))
    #print(*data, sep='\n')
    for i in range(1, 1+steps):
        data = enhance(keystring, data)
        print('completed step {}'.format(i))
        #print('image data after step {}: {} rows x {} cols:'.format(i, len(data), len(data[0])))
        #print(*data, sep='\n')
        if i == 2:
            count = sum([1 if c=='#' else 0 for row in data[steps:-steps] for c in row[steps:-steps]])
            print('found {} lit pixels'.format(count))

    #print('final image data after step {}: {} rows x {} cols:'.format(i, len(data), len(data[0])))
    #print(*data, sep='\n')

    count = sum([1 if c=='#' else 0 for row in data[steps:-steps] for c in row[steps:-steps]])
    print('found {} lit pixels'.format(count))
