import argparse
import re


# REKURZE CVICENI
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument('-i', default='05', type=str, help='input file')
    args = parser.parse_args()

    with open(args.i, 'r') as f:
        data = [[bag_rules if i == 0 else bag_rules
                 for i, bag_rules in enumerate(line.split(' contain '))] for line in f.read().replace('.', '').split('\n')]

        rules = {}
        for bag in data:
            if bag[0] not in rules:
                rules[bag[0].replace('bags', 'bag')] = bag[1].replace('bags', 'bag')
            else:
                rules[bag[0].replace('bags', 'bag')] += (' ' + bag[1].replace('bags', 'bag'))
                # rules[bag[0]].extend(bag[1])
        print(rules)

        bags = ['shiny gold bag']
        for bag in bags:
            # print(f"Current: {bag}\n")
            for k, v in rules.items():
                if re.search('\d+ ' + bag, v):
                    bags.append(k.replace('bags', 'bag'))
                    # print(f"Valid: {bag} in {k}")

        print(f"Task 1: {len(set(bags))-1}")

        total = 0
        def rec(bag, n, koef):
            global total
            print("IN", bag, n, koef, total)
            for i in rules[bag].split(', '):
                nn, nbag = i.split(' ', 1)
                if nn != 'no':
                    total += koef * int(nn)
                    print(f"Calling {nbag} with params ({int(nn)}, {koef*int(nn)}) with total: {total}")
                    rec(nbag, int(nn), koef * int(nn))

        rec('shiny gold bag', 1, 1)
        print(f"Task 2: {total}")
