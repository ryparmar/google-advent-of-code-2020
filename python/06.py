import argparse
import re
from collections import Counter
import itertools

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument('-i', default='05', type=str, help='input file')
    args = parser.parse_args()

    with open(args.i, 'r') as f:
        data = [[[vote for vote in person]
                 for person in group.split('\n')] for group in f.read().split('\n\n')]
        # print(data)

        # Task 1
        data_uniq = [len(set(itertools.chain.from_iterable(group)))
                     for group in data]
        print(f"Task 1: Sum of counts: {sum(data_uniq)}")

        # Task 2
        # assume that single person cannot answer single letter twice
        # e.g.  abb  -- line is invalid/impossible
        persons = [len(group) for group in data]
        counts = [Counter(list(itertools.chain.from_iterable(group)))
                  for group in data]
        # print(counts)
        task2 = [p == count[c]
                 for p, count in zip(persons, counts) for c in count]
        print(f"Task 2: Sum of counts: {sum(task2)}")
        # print(task2)
