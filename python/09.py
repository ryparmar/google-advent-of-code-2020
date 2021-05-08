import argparse
import re

# Dynamic Programming
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument('-i', default='08', type=str, help='input file')
    args = parser.parse_args()

    with open(args.i, 'r') as f:
        data = [int(line.strip()) for line in f.read().split('\n')]

    mat = [[i+ii for ii in data] for i in data]

    # Task 1
    preamb = 25
    
    idx, num = 0, 0  # for task 2
    for i, n in enumerate(data[preamb:]):
        found = False
        for ii, nn in enumerate(mat[i:i+preamb]):
            for iii, nnn in enumerate(nn[i:i+preamb]):
                if (n == nnn and ii != iii) or i+preamb > len(data):
                    found = True
                    continue
            if found:
                continue
        if not found:
            idx = i + preamb
            num = n
            print(f"Task 1: {n}")
            break

    # Task 2
    for i, n in enumerate(data[:(idx-1)]):
        ii = i+1
        found = False
        while sum(data[i:ii]) <= num and ii < idx:
            if sum(data[i:ii]) == num:
                print(f"Task 2: {min(data[i:ii]) + max(data[i:ii])}")
                found = True
                break
            if sum(data[i:ii]) < num:
                ii += 1
        if found:
            break
