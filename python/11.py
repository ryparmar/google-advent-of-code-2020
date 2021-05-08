import argparse
import copy
import itertools

# Returns 8 possible directions adjacent to row, col coordinates
def get_adj(seats, row, col):
    adj = []
    for pos in [(i, j) for i in (-1,0,1) for j in (-1,0,1) if not (i == j == 0)]:
        if 0 <= row+pos[0] < len(seats) and 0 <= col+pos[1] < len(seats):
            adj.append((row+pos[0], col+pos[1]))
    return adj

DIRECTIONS = [(i, j) for i in (-1,0,1) for j in (-1,0,1) if not (i == j == 0)]

def task1(seats):
    ret = copy.deepcopy(seats)
    changes = 0
    for row, col in itertools.product(range(len(seats)), range(len(seats))):
        if seats[row][col] == 0 or seats[row][col] == 1:
            adj = get_adj(seats, row, col)
            if seats[row][col] == 0 and all([1 if seats[a[0]][a[1]] != 1 else 0 for a in adj]):
                ret[row][col] = 1
                changes += 1
            elif seats[row][col] == 1 and sum([1 if seats[a[0]][a[1]] == 1 else 0 for a in adj]) >= 4:
                ret[row][col] = 0
                changes += 1
    return ret, changes


def get_first_seat(seats, row, col, drow, dcol):
    """
    seats -- seats grid
    row -- current row seat
    col -- curent col seat
    drow -- one of the eight possible directions / change in row
    dcol -- one of the eight possible directions / change in col
    """
    coef = 1
    while 0 <= (row + drow*coef) < len(seats) and 0 <= (col + dcol*coef) < len(seats):
        if seats[row + drow*coef][col + dcol*coef] == 0:  #empty
            return 0
        elif seats[row + drow*coef][col + dcol*coef] == 1:  #occupied
            return 1
        else:
            coef += 1
        # print(f"CHECK: {len(seats), len(seats[0])}")
        # print(f"{row} {drow*coef} {col}  {dcol*coef}")
        # print(f"{row + drow*coef} {dcol + dcol*coef}")
    return 0


def task2(seats):
    ret = copy.deepcopy(seats)
    changes = 0
    for row, col in itertools.product(range(len(seats)), range(len(seats))):
        if seats[row][col] == 0 or seats[row][col] == 1:
            if seats[row][col] == 0 and all([1 if get_first_seat(seats, row, col, a[0], a[1]) != 1 else 0 for a in DIRECTIONS]):
                ret[row][col] = 1
                changes += 1
            elif seats[row][col] == 1 and sum([get_first_seat(seats, row, col, a[0], a[1]) for a in DIRECTIONS]) >= 5:
                ret[row][col] = 0
                changes += 1
    return ret, changes

def print_nice(ll):
    for l in ll:
        print(f"{(' '.join([str(i) for i in l])).replace('-1', '.').replace('1', '#').replace('0', 'L')}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument('-i', default='11', type=str, help='input file')
    args = parser.parse_args()

    with open(args.i, 'r') as f:
        data = [
                [int(c.replace('L', '0').replace('.', '-1').replace('#', '1')) for c in line.strip()]
            for line in f.read().split('\n')
        ]
    # print_nice(data)

    # Task 1
    seats = copy.deepcopy(data)
    changes = 1
    it = 0
    while changes > 0:
        seats, changes = task1(seats)
        it += 1
        # print(f"Iterations: {it}")
        # print_nice(seats)

    print(f"Task 1: {sum([1 if seat == 1 else 0 for l in seats for seat in l])}")
    print(f"Iterations: {it}")

    seats = copy.deepcopy(data)
    changes = 1
    it = 0
    print(f"Iterations: {it}")
    print_nice(seats)
    while changes > 0:
        seats, changes = task2(seats)
        it += 1
        # print(f"Iterations: {it}")
        # print_nice(seats)

    print(f"Task 2: {sum([1 if seat == 1 else 0 for l in seats for seat in l])}")
    print(f"Iterations: {it}")
