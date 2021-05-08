import argparse
import copy
import itertools


def task1(data):
    ship = {'deg': 0,
            'F': 'E',
            'N': 0,
            'S': 0,
            'E': 0,
            'W': 0}

    for l in data:
        if l[0] in ['L', 'R']:
            if l[0] == 'L':
                deg = r2d(ship['deg'], +int(l[1:]))
            else:
                deg = r2d(ship['deg'], -int(l[1:]))
            if not 0 <= deg <= 360:
                print(l, ship['deg'], deg)
            ship['deg'] = deg
            ship['F'] = r[deg]
        elif l[0] == 'F':
            ship[ship['F']] += int(l[1:])
        else:
            ship[l[0]] += int(l[1:])
    return ship

def shift(seq, n=0):
    """
        SHIFT LEFT: N E S W; n=1 -> E S W N  
        SHIFT RIGHT: N E S W; n=-1 -> W N E S 
    """
    a = abs(n) % len(seq)
    if n >= 0:
        return seq[n:] + seq[:n]
    else:
        return seq[-a:] + seq[:-a]


def task2(data):
    ship = {'N': 0,
            'S': 0,
            'E': 0,
            'W': 0}
    to_id = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
    wp = [1, 10, 0, 0]  # N E S W


    for l in data:
        if l[0] in ['L', 'R']:
            shift_n = int(l[1:])
            if l[0] == 'L':
                wp = shift(wp, shift_n)  # shift left; anti-clockwise == L
            else:
                wp = shift(wp, -shift_n)  # shift righ; clockwise == R

        elif l[0] == 'F':
            ship['N'] += int(l[1:]) * wp[0]
            ship['E'] += int(l[1:]) * wp[1]
            ship['S'] += int(l[1:]) * wp[2]
            ship['W'] += int(l[1:]) * wp[3]
        else:
            wp[to_id[l[0]]] += int(l[1:])
    return ship

# NICE SOLUTON USING IMAGINARY NUMBERS
# Imaginary numbers makes the addition much easier than breaking it into x/y coordinates. Clockwise and counter
# clockwise rotations are a matter swapping real / imaginary parts and negating one or the other depending on the rotation.
from collections import deque

def imaginary(data):
    facing = deque('ESWN')
    steps = {'N': 1j, 'E': 1, 'S': -1j, 'W': -1}
    p1, p2 = 0, 0
    waypoint = 10+1j

    for line in data:
        op, arg = line[0], int(line[1:].strip())
        val = arg // 90
        if op == 'L':
            facing.rotate(val)
            for _ in range(val):
                waypoint = complex(-waypoint.imag, waypoint.real)
        if op == 'R':
            facing.rotate(-val)
            for _ in range(val):
                waypoint = complex(waypoint.imag, -waypoint.real)
        if op == 'F':
            step = steps.get(facing[0])
            p1 += step * arg
            p2 += waypoint * arg
        if op in facing:
            step = steps.get(op)
            p1 += step * arg
            waypoint += step * arg

    print(f"Part 1 Answer: {int(abs(p1.real) + abs(p1.imag))}")
    print(f"Part 2 Answer: {int(abs(p2.real) + abs(p2.imag))}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument('-i', default='12', type=str, help='input file')
    args = parser.parse_args()

    with open(args.i, 'r') as f:
        data = [line.strip() for line in f.read().split('\n')]

    r = {0: 'E',
        360: 'E',
        90: 'N',
        180: 'W',
        270: 'S'}

    def r2d(cur, change):
        if cur + change < 0:
            return 360 + (cur + change)
        elif cur + change > 360:
            return cur + change - 360
        else:
            return cur + change 

    ship = task1(data)
    print(f"Task 1: {abs(ship['E']-ship['W']) + abs(ship['S']-ship['N'])}")

    ship = task2(data)
    print(f"Task 2: {abs(ship['E']-ship['W']) + abs(ship['S']-ship['N'])}")


    imaginary(data)


