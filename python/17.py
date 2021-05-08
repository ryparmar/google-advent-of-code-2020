import argparse
import copy
import itertools
import sys


get_neighbours()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument('-i', default='17', type=str, help='input file')
    args = parser.parse_args()

    with open(args.i, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    print(data)

