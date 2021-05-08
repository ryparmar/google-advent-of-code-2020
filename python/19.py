import argparse
import itertools
import sys
import re


class Tree:
    def __init__(self, rules: list, messages: list):
        self.rules = rules if rules else None
        self.ret = []
        self.root = rules[0] if rules else None
        self.messages = messages

    def parse(self, rule):
        if ' | ' in rule:
            return f" ( {rule} ) "
        else:
            return ' ' + rule.strip('"') + ' '

    def generate(self, rule):
        ## GENERATE ONE LONG REGEXP-LIKE RULE -- Turing Machine like approach
        parsed, ret = False, ''
        if ' | ' in rule:  # if the root rule contains |
            ret += f"{ret} ( {rule} ) "
        else:
            ret = rule
        print("ROOT RULE:", rule, " RETURN:", ret)

        while not parsed:
            change, nret = False, ''
            for sub in ret.split():
                if sub not in ('(', ')') and sub.isnumeric():
                    nret += self.parse(self.rules[int(sub)])
                    change = True
                elif sub:
                    nret += ' ' + sub
            
            ret = re.sub('\s+', ' ', nret)  # remove multi-spaces
            print("RET", ret)
            if not change:
                parsed = True

        return ret
        
    def validate(self):
        regex = self.generate(self.root)
        cnt = 0
        for m in self.messages:
            match = re.fullmatch(regex, m, flags=re.VERBOSE)
            if match:
                cnt += 1
                # print(m)
        print(f"COUNT OF VALID MESSAGES: {cnt}")

        ## BACKTRACK try
        # print("RULE:", rule)
        # if ' | ' in rule:
        #     for sub in rule.split(' | '):
        #         self.parse(sub, ret)
        # else:
        #     # if isinstance(ret, list):
        #     #     for
        #     for subsub in rule.split():
        #         print("subsub", subsub)
        #         if self.rules[int(subsub)].startswith('"'):
        #             print("adding", subsub)
        #             ret += subsub #self.rules[int(subsub)].strip('"')
        #         else:
        #             tmp = self.parse(self.rules[int(subsub)], ret)
        #             if isinstance(tmp, list):
        #                 ret = [ret + i for i in tmp]
        #             elif isinstance(tmp, str):
        #                 ret += tmp
        #             else:
        #                 ret = ret
        
        #     print("RET:", ret) 
        #     return ret

def generate_valid_combinations(rules):
    for rule in rules:
        for sub in rule.split(' | '):
            yield generate_valid_combinations(sub)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument('-i', default='../192', type=str, help='input file')
    args = parser.parse_args()

    with open(args.i, 'r') as f:
        rules, messages = {}, []
        for line in f:
            if ':' in line:
                tmp = line.split(':')
                rules[int(tmp[0])] = tmp[1].strip()
            elif line.strip():
                messages.append(line.strip())
    
    print(rules)
    print(messages)

    t = Tree(rules, messages)
    t.validate()

    # for rule in rules:
    #     for r in parse(rule):
    #         print(r)
    # parse(rules[1])

