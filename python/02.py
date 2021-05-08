import argparse
from collections import Counter


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument('-i', type=str, help='input file')
    args = parser.parse_args()

    with open(args.i, 'r') as f:
        data = []
        valids, valids2 = 0, 0
        for i in f:
            a, b, pwd = i.split()
            _min, _max = map(int, a.split('-'))
            policy = b.strip(':')
            counts = Counter(pwd)

            # Task 1
            if (policy not in counts and _min == 0) or (policy in counts and (counts[policy] >= _min and counts[policy] <= _max)):
                valids += 1

            # Task 2
            if (pwd[_min-1] == policy and pwd[_max-1] != policy) or (pwd[_min-1] != policy and pwd[_max-1] == policy):
                valids2 += 1


        print(f"Task1: Count of valids: {valids}")
        print(f"Task2: Count of valids: {valids2}")

