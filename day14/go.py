#!/usr/bin/python3

import sys
import collections

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        template = f.readline().strip()
        empty = f.readline()
        rules = dict((x.strip(), y.strip())
                     for x, y in (line.strip().split(' -> ')
                     for line in f.readlines()))

    #print('rules {}'.format(rules))

    backup = template
    #print('template {}'.format(template))

    for step in range(10):
        pos = 0
        while pos < len(template)-1:
            sequence = template[pos:pos+2]
            template = template[:pos+1] + rules[sequence] + template[pos+1:]
            pos += 2
        #print('after step {}: length is {}'.format(step + 1, len(template)))

    counter = collections.Counter(template)
    m = max(counter, key = counter.get)
    l = min(counter, key = counter.get)
    print('most is {} with count {}, least is {} with count {}'.format(m, counter[m], l, counter[l]))
    print('delta is {}'.format(counter[m] - counter[l]))

    template = backup
    #print('template {}'.format(template))

    pairs = {}
    for i in range(len(template) - 1):
        pair = template[i:i+2]
        pairs[pair] = pairs.setdefault(pair, 0) + 1
    for step in range(40):
        newpairs = {}
        for pair in pairs:
            count = pairs[pair]
            n = rules[pair]
            l = pair[0] + n
            r = n + pair[1]
            newpairs[l] = newpairs.setdefault(l, 0) + count
            newpairs[r] = newpairs.setdefault(r, 0) + count
        pairs = newpairs

    #print('found pairs {}'.format(pairs))

    counts = {}
    counts[template[-1]] = 1
    for pair in pairs:
        c = pair[0]
        counts[c] = counts.setdefault(c, 0) + pairs[pair]

    m = max(counts, key = counts.get)
    l = min(counts, key = counts.get)
    print('most is {} with count {}, least is {} with count {}'.format(m, counts[m], l, counts[l]))
    print('delta is {}'.format(counts[m] - counts[l]))
