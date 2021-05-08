import argparse
import itertools
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument('-i', default='../201', type=str, help='input file')
    args = parser.parse_args()

    with open(args.i, 'r') as f:
        tiles = {}
        for tile in f.read().split('\n\n'):
            cur_tile = None
            for line in tile:
                if line.startswith('Tile'):
                    cur_tile = int(line.split().strip(':'))
                    tiles[cur_tile] = []
                elif line.strip():
                    tiles[cur_tile].append(line)

            # print(tiles[cur_tile])


