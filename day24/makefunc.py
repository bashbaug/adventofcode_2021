#!/usr/bin/python3

import sys

def makepython(lines):
    spos = 0
    for line in lines:
        command = line.strip().split()
        print('    # {}'.format(line.strip()))
        if command[0] == 'inp':
            print('    {} = int(inputstr[{}])'.format(command[1], spos))
            spos += 1
        elif command[0] == 'add':
            print('    {} += {}'.format(command[1], command[2]))
        elif command[0] == 'mul':
            print('    {} *= {}'.format(command[1], command[2]))
        elif command[0] == 'div':
            print('    {} //= {}'.format(command[1], command[2]))
        elif command[0] == 'mod':
            print('    {} %= {}'.format(command[1], command[2]))
        elif command[0] == 'eql':
            print('    {} = 1 if {} == {} else 0'.format(command[1], command[1], command[2]))
        else:
            print('unknown command {}!'.format(command[0]))

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    makepython(lines)
