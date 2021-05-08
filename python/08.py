import argparse
import re

# Backtracking
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument('-i', default='08', type=str, help='input file')
    args = parser.parse_args()

    with open(args.i, 'r') as f:
        data = [(line.split()[0], int(line.split()[1])) for line in f.read().split('\n')]

    print(data)

    # Task 1
    acc, pos = 0, 0
    visited = []

    def parse(data, pos, acc, switch=False):
        act = data[pos][0]
        if switch:
            if data[pos][0] == 'jmp':
                act = 'nop'
            elif data[pos][0] == 'nop':
                act = 'jmp'

        if act == 'nop':
            return pos+1, acc
        elif act == 'jmp':
            return pos + data[pos][1], acc
        elif act == 'acc':
            return pos+1, acc + data[pos][1]
        # return pos+1, acc if act == 'nop' else pos + data[pos][1], acc if act == 'jmp' else pos+1, acc + data[pos][1]

    while True:
        if pos not in visited and pos >= 0 and pos < len(data):
            visited.append(pos)
            pos, acc = parse(data, pos, acc)
        else:
            break
    print(f"Task 1: {acc}")

    import copy
    # Task 2
    # Slo by take vygenerovat vsechny mozne permutace s prave jednou zmenou/swapem v jmp/nop
    def generate(data):
        yield data
        for i, ii in enumerate(data):
            if ii[0] == 'jmp':
                ret  = copy.deepcopy(data)
                ret[i] = ('nop', ii[1])
                yield ret
            elif ii[0] == 'nop':
                ret  = copy.deepcopy(data)
                ret[i] = ('jmp', ii[1])
                yield ret

    for path in generate(data):
        # print(path)
        acc, pos = 0, 0
        visited = []
        while True:
            if pos not in visited and pos >= 0 and pos < len(path):
                visited.append(pos)
                pos, acc = parse(path, pos, acc)
                if pos > len(path) - 1:
                    print(f"Task 2: {acc}  {path}")
            else:
                break



    # acc, pos = 0, 0
    # finished = False
    # def backtrack(pos, acc, visited=[]):
    #     print(f"Check: {pos} {acc} {visited}")
    #     if pos in visited or pos < 0 or pos >= len(data):
    #         return 
    #     if pos == len(data)-1:
    #         pos, acc = parse(pos, acc)
    #         print(f"Task 2: {acc}")
    #         return
    #     else:
    #         pos1, acc1 = parse(pos, acc)
    #         pos2, acc2 = parse(pos, acc, True)
    #         backtrack(pos1, acc1, visited + [pos])
    #         backtrack(pos2, acc2, visited + [pos] )

    # backtrack(pos, acc)