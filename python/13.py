import argparse
import copy
import itertools

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument('-i', default='13', type=str, help='input file')
    args = parser.parse_args()

    with open(args.i, 'r') as f:
        t0 = int(f.readline().strip())
        idxs = [i.strip() for i in f.readline().strip().split(',')]
        ids = [int(i.strip()) for i in idxs if i != 'x']
        print(t0, ids, idxs)
        
        cur_t = t0
        while True:
            waits = [cur_t % t for t in ids]
            if 0 in waits:
                i = waits.index(0)
                wait = cur_t - t0
                chosen_id = ids[i]
                break
            else:
                cur_t += 1 
        
        print(f"Task 1: {wait * chosen_id}\nwaiting time: {wait}\nchosen id: {chosen_id}")

        
        n = idxs.index(str(max(ids)))
        a = abs(n) % len(idxs)
        if n >= 0:
            idxs = idxs[n:] + idxs[:n]
        print(idxs)

        cur_t = t0
        while cur_t % 
        while True:
            if all([cur_t + int(idxs.index(str(idx))) % idx == 0 and cur_t + int(idxs.index(str(idx))) > idx for idx in ids]):
                break
            else:
                cur_t += max(ids)
        print(f"Task 2: {cur_t}")   
