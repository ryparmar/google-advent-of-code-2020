from itertools import combinations
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument('-i', type=str, help='input file')
    args = parser.parse_args()

    with open(args.i, 'r') as f:
        data = [int(i.strip()) for i in f.readlines()]

    # Task 1
    for i, ii in combinations(data, 2):
        if i + ii == 2020:
            print(i*ii)

    # Task 1 - less elegant
    # found = False
    # for i in data:
    #     for ii in data:
    #         if i+ii == 2020:
    #             print(i*ii)
    #             found = True
    #             break
    #     if found:
    #         break

    # Task 2
    for i, ii, iii in combinations(data, 3):
        if i + ii + iii == 2020:
            print(i*ii*iii)
    
    