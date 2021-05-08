import argparse
import copy
import itertools

def masked1(x, mask):
    assert len(str(x)) == len(str(mask))
    ret = ""
    for i, v in enumerate(mask):
        if v == '1':
            ret += '1'
        elif v == '0':
            ret += '0'
        else:
            ret += x[i]
    return ret

def initialize1(memory, mask, commands):
    for c in commands:
        memory[c[0]] = masked1(f'{c[1]:036b}', mask)

def masked2(x, mask):
    # print(len(str(x)), len(str(mask)))
    assert len(str(x)) == len(str(mask))
    ret = ""
    for i, v in enumerate(mask):
        if v == '1':
            ret += '1'
        elif v == '0':
            ret += x[i]
        else:
            ret += 'X'
    return ret

def combinations(masked):
    l = masked.count('X')
    ret = []
    for comb in itertools.product('01', repeat=l):
        # print(f"comb: {comb}")
        c, r = 0, ""
        for m in masked:
            if str(m) == 'X':
                r += comb[c]
                c += 1
            else:
                r += str(m)
        ret.append(r)
    # print(ret)
    return ret


def initialize2(memory, mask, commands):
    for cmd in commands:
        # print(f"CMD: {cmd}")
        for comb in combinations(masked2(f'{cmd[0]:036b}', mask)):
            memory[comb] = f'{cmd[1]:036b}'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument('-i', default='14', type=str, help='input file')
    args = parser.parse_args()
    
    # Task 1
    with open(args.i, 'r') as f:
        mask, commands = "", []
        memory = {}
        for line in f.readlines():
            if line.strip().startswith('mask'):
                if mask and len(commands) > 0:
                    # print(f"mask: {mask}\ncommands: {commands}")
                    initialize1(memory, mask, commands)
                    commands = []
                mask = line.strip().split(' = ')[1]
            else:
                tmp1, tmp2 = line.replace('mem[', '').replace(']', '').strip().split(' = ')
                commands.append((int(tmp1), int(tmp2)))

        initialize1(memory, mask, commands)
        print(f"Task 1: {sum([int(v, 2) for _, v in memory.items()])}")

    # Task 2
    with open(args.i, 'r') as f:
        mask, commands = "", []
        memory = {}
        for line in f.readlines():
            if line.strip().startswith('mask'):
                if mask and len(commands) > 0:
                    initialize2(memory, mask, commands)
                    commands = []
                mask = line.strip().split(' = ')[1]
            else:
                tmp1, tmp2 = line.replace('mem[', '').replace(']', '').strip().split(' = ')
                commands.append((int(tmp1), int(tmp2)))

        initialize2(memory, mask, commands)
        # print([int(v, 2) for _, v in memory.items()])
        # print(len(memory.items()), memory.items())
        print(f"Task 2: {sum([int(v, 2) for _, v in memory.items()])}")    