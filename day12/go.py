#!/usr/bin/python3

import sys

def traverse(paths, visited, doubled, location, path):
    ret = 0
    mypath = path.copy()
    mypath.append(location)
    if location == 'end':
        #print(mypath)
        return 1
    myvisited = visited.copy()
    myvisited.append(location)
    for n in paths[location]:
        if n.isupper():
            ret += traverse(paths, myvisited, doubled, n, mypath)
        elif not n in myvisited:
            ret += traverse(paths, myvisited, doubled, n, mypath)
        elif not doubled and n != 'start':
            ret += traverse(paths, myvisited, True, n, mypath)
    return ret

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    paths = {}
    for line in lines:
        path = line.strip().split('-')
        paths.setdefault(path[0], []).append(path[1])
        paths.setdefault(path[1], []).append(path[0])

    #print(paths)

    count = traverse(paths, [], True, 'start', [])

    print('only visiting once: count is {}'.format(count))

    count = traverse(paths, [], False, 'start', [])

    print('visiting one twice: count is {}'.format(count))
