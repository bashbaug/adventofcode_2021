#!/usr/bin/python3

import sys

# Find the distance between all of the beacons for a scanner
def calculateDistances(scanner):
    for beacon in scanner:
        x1, y1, z1 = scanner[beacon]['pos']
        scanner[beacon]['distances'] = set()
        for ob in [bx for bx in scanner if bx != beacon]:
            x2, y2, z2 = scanner[ob]['pos']
            distance = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
            scanner[beacon]['distances'].add(distance)

# Find matching beacons and return the scanner they are from
def findMatches(scanners):
    for os in [sx for sx in scanners if sx != 0]:
        matches = []
        for beacon in scanners[0]:
            for ob in scanners[os]:
                bd = scanners[0][beacon]['distances']
                od = scanners[os][ob]['distances']
                if len(bd.intersection(od)) >= 11:
                    matches.append({'beacon': beacon, 'ob': ob})
                    if len(matches) == 12:
                        return os, matches

# Transform the beacons from otherscanner and add to scanner zero
# Returns the offset of the other scanner from scanner zero
def transform(otherscanner, matches, scanners):
    for n in range(1, 12):
        db0, dbn = [scanners[0][matches[i]['beacon']]['pos'] for i in (0, n)]
        sb0, sbn = [scanners[otherscanner][matches[i]['ob']]['pos'] for i in (0, n)]
        ddelta = [db0[i] - dbn[i] for i in (0, 1, 2)]
        sdelta = [sb0[i] - sbn[i] for i in (0, 1, 2)]
        # We need three unique deltas to compute the orientation
        if len(set(ddelta)) == 3 and len(set(sdelta)) == 3 and \
           not 0 in ddelta and not 0 in sdelta:
            break

    index = [sdelta.index(ddelta[i]) if ddelta[i] in sdelta else sdelta.index(-ddelta[i]) for i in (0, 1, 2)]
    flip = [ddelta[i] // sdelta[index[i]] for i in (0, 1, 2)]

    offset = [db0[i] - (sb0[index[i]] * flip[i]) for i in (0, 1, 2)]

    known = [scanners[0][b]['pos'] for b in scanners[0]]
    for b in scanners[otherscanner]:
        beacon = [scanners[otherscanner][b]['pos'][index[i]] * flip[i] + offset[i] for i in (0, 1, 2)]
        if beacon not in known:
            scanners[0][len(scanners[0])] = {'pos': beacon}
    return offset

# Creates the map of all beacons by merging into scanner zero
# Returns the offset of all scanners from scanner zero
def createMap(scanners):
    offsets = [[0, 0, 0]]
    while len(scanners) > 1:
        otherscanner, matches = findMatches(scanners)
        offsets.append(transform(otherscanner, matches, scanners))
        del scanners[otherscanner]
        calculateDistances(scanners[0])
    return offsets

# Find the maximum distance between scanners
def findMaxDistance(offsets):
    m = 0
    for i in range(len(offsets)):
        for j in range(i + 1, len(offsets)):
            m = max(m, sum([abs(offsets[i][k] - offsets[j][k]) for k in (0, 1, 2)]))
    return m

if __name__ == '__main__':
    scanners = {}
    with open(sys.argv[1]) as f:
        numscanners = 0
        for line in f:
            if line.startswith('--- scanner '):
                scanners[numscanners] = {}
                count = 0
            elif line.strip():
                scanners[numscanners][count] = {'pos': [int(x) for x in line.split(',')]}
                count += 1
            else:
                numscanners += 1

    for s in scanners:
        calculateDistances(scanners[s])

    offsets = createMap(scanners)

    print('number of unique beacons is {}'.format(len(scanners[0])))
    print('longest distance is {}'.format(findMaxDistance(offsets)))
