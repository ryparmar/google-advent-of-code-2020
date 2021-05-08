import argparse
from collections import Counter

# Dynamic Programming
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument('-i', default='10', type=str, help='input file')
    args = parser.parse_args()

    with open(args.i, 'r') as f:
        data = sorted([
            int(line.strip())
            for line in f.read().split('\n')
        ])

    print(data)
    diff = [ii-i for i, ii in zip(data[:-1], data[1:])]
    diff.extend([data[0], 3])
    print(diff)

    counted = Counter(diff)
    print(counted)
    print(f"Task 1: {counted[1]*counted[3]}")
    
    # tmp, N = 0, 0
    # for i, n in enumerate(data):
    #     if tmp == 3:
    #         N += 2
    #         tmp = 0
    #     elif diff[i] != 1 and tmp == 2:
    #         N += 1
    #         tmp = 0

    #     if diff[i] == 1:
    #         tmp += 1
    #     else:
    #         tmp = 0

    # combinations = 0
    # import math
    # for n in range(N):
    #     print((math.factorial(n) / (math.factorial(N-n) * math.factorial(n))))
    #     combinations += (math.factorial(N) / (math.factorial(N-n) * math.factorial(n)))

    # Misinterpret assignment? Did not understand it well. 
    # Solution took from here: https://github.com/elvinyhlee/advent-of-code-2020-python/blob/master/day10.py
    # when looking for hints. Really nice dynamic programming approach, which I havent though of.
    # I thought of drawing a graph and looking for paths resp. enumerating them or then directly compute the combinations
    # which a I have tried, but did not work out
    dp = Counter()
    dp[0] = 1

    for jolt in data:
        dp[jolt] = dp[jolt - 1] + dp[jolt - 2] + dp[jolt - 3]
        print(f"jolt: {jolt}\ndp: {dp}")

    print(dp)
    dp[data[-1]]
    print(f"Task 2: {dp[data[-1]]}")