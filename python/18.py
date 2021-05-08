import argparse
import copy
import itertools
import sys


def evaluate(exp):
    print(f"Eval: {exp.replace('(', '').replace(')', '')}")
    l, r, op = '', '', ''
    for e in exp.replace('(', '').replace(')', ''):
        print(e)
        if op and e in ['*', '+']:
            l = int(l)+int(r) if op == '+' else int(l)*int(r)
            r = ''

        if e == '+':
            op = '+'
        elif e == '*':
            op = '*'
        else:
            if not op:
                l += e
            else:
                r += e

    if op not in ['+', '*']:
        print("WRONG OPERATOR!", op)
    return int(l)+int(r) if op == '+' else int(l)*int(r)        


def replace_bracket(exp, lb, rb):
    ret, i = "", 0
    while i < len(exp):
        if i < lb or i > rb:
            ret += exp[i]
            i += 1
        else:
            ret += str(evaluate(exp[lb:rb+1]))
            i = rb+1
    return ret


def parse(exp):
    print("Expression: ", exp)
    if '(' in exp or ')' in exp:
        lb, rb, br = [], [], []
        for i, e in enumerate(exp):
            if e == '(':
                lb.append(i)
            if e == ')':
                rb.append(i)
                br.append((lb[-1], i))
        br[-1] = (lb[0], rb[-1])
        rb.reverse()
        print(lb, rb)
        print(f"brackets: {br}")

        nexp = copy.deepcopy(exp)
        for l, r in br:
            print(f"brackets: {l} {r}")
            nexp = replace_bracket(exp, l, r)
            print(f"replaced: {nexp}")
        return evaluate(nexp)
    else:
        return evaluate(exp)
    # print(f"RESULT: {evaluate(exp)}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument('-i', default='18', type=str, help='input file')
    args = parser.parse_args()
    print(parse('2 * (3 + (4 * 5))')) #.replace(' ', '')))
    print(parse('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')) #.replace(' ', '')))
    # with open(args.i, 'r') as f:
    #     data = [line.strip() for line in f.readlines()]
    # print(data)