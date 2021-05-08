import argparse
import re

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument('-i', default='05', type=str, help='input file')
    args = parser.parse_args()

    with open(args.i, 'r') as f:
        data = [str(seat).strip() for seat in f.readlines()]
        print(data)

    # Task 1
    def parse_seat(seat, num):
        for c in seat:
            rng = num[1] + 1 - num[0]
            if c == 'F' or c == 'L':  # take lower half
                num[1] = num[1] - rng / 2
            elif c == 'B' or c == 'R':  # take upper half
                num[0] = num[0] + rng / 2
            else:
                print("ERROR INPUT!")
        assert num[0] == num[1]
        return num[0]

    def get_row(seat):
        assert len(seat) == 7
        return parse_seat(seat, [0, 127])

    def get_column(seat):
        assert len(seat) == 3
        return parse_seat(seat, [0, 7])

    def get_id(seat):
        return get_row(seat[:7]) * 8 + get_column(seat[-3:])

    ids = [get_id(seat) for seat in data]
    print(f"Task 1: Highest seat ID: {max(ids)}")

    # Task 2
    ids = sorted(ids, reverse=True)
    diffs = [i-ii for i, ii in zip(ids[:-1], ids[1:])]
    my_idx = diffs.index(2)
    my_id = ids[my_idx] - 1
    print(f"Sorted: {ids}\nDiffs: {diffs}")
    print(f"Task 2: My seat ID: {my_id}")
