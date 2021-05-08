import argparse
import copy
import itertools

def get_error_rate(t, r):
    return 0 if r[0] <= t <= r[1] else t

def is_valid(t, rules):
    if isinstance(rules, list) and isinstance(rules[0], list):
        errors = [get_error_rate(t, r) for group in rules for r in group]
    elif isinstance(rules, list):
        errors = [get_error_rate(t, r) for r in rules]
    if all(errors): # all the rules in a single group not satisfied
        return False, [i for i in errors if i][0]
    else:
        return True, 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument('-i', default='16', type=str, help='input file')
    args = parser.parse_args()

    with open(args.i, 'r') as f:
        my_ticket, nearby_tickets, ranges, fields = [], [], [], []
        for line in f.readlines():
            if line.strip():
                if line[0].isdigit() and not my_ticket:
                    my_ticket = [[int(i) for i in line.split(',')]]
                elif line[0].isdigit() and my_ticket:
                    nearby_tickets.append([int(i) for i in line.split(',')])

                if not my_ticket and not nearby_tickets and len(line.split(': ')) > 1:
                    fields.append(line.split(': ')[0])
                    ranges.append([(int(rule.split('-')[0]), int(rule.split('-')[1])) for rule in line.split(': ')[1].strip().split(' or ')])

        print(f"my: {my_ticket}\nnearby: {nearby_tickets}\nranges: {ranges}")

    all_tickets = my_ticket + nearby_tickets
    validation = [[is_valid(field, ranges)[1] for field in t] for t in all_tickets]
    ticket_errors = [sum(i) for i in validation]
    print(f"Task 1: {sum(ticket_errors)}")

    # Task 2
    valid_tickets = [all_tickets[i]
                    for i in range(len(all_tickets))
                    if ticket_errors[i] == 0]
    print("valid: ", valid_tickets)
    print("validation: ", validation)
    print("errors: ", ticket_errors)
    print(fields)

    # Generate valid choices rule-position
    rule2pos = {i: [] for i, _ in enumerate(fields)}
    for pos in range(len(all_tickets[0])):
        vals = [i[pos] for i in valid_tickets]
        # print(f"pos: {pos} vals: {vals}")
        for i_f, field in enumerate(ranges):
            if all([is_valid(i, field)[0] for i in vals]):
                rule2pos[i_f].append(pos)
    print(rule2pos)

    # Reduce and choose rule-position
    final_r2p = {}
    while len(final_r2p) < len(fields):
        for k, v in rule2pos.items():
            if len(v) == 1:
                final_r2p[k] = v.pop()
                for kk, vv in rule2pos.items():
                    if vv and final_r2p[k] in vv: #rule2pos[kk]:
                        vv.remove(final_r2p[k])
    print(f"final: {final_r2p}")
    print(f"Task 2: {[my_ticket[0][final_r2p[i]] for i, f in enumerate(fields) if f.startswith('departure')]}")


            
            
    
        