import argparse
import copy
import itertools
import sys

# The sequence is called the Van Eck sequence - quite an interesting one
# https://www.youtube.com/watch?v=etMJxB-igrc
def memory_game(start, N):
    last_spoken = {num: i  for i, num in enumerate(start)}
    print(last_spoken)

    last = start[-1]
    for i in range(len(start)-1, N):
        if last not in last_spoken:
            diff = 0
        else:
            diff = i - last_spoken[last]
        
        last_spoken[diff] = i
        last = diff
        print(i, diff)
        print(last_spoken)
    return last

# inspired from: https://github.com/mariothedog/Advent-of-Code-2020/blob/main/Day%2015/day_15.py
def memory_game2(numbers, final_turn):
	turn_spoken = {num: i + 1 for i, num in enumerate(numbers[:-1])}

	next_num = numbers[-1]
	for turn_num in range(len(numbers)+1, final_turn+1):
		last_turn_num = turn_num - 1
		if next_num in turn_spoken:
			spoken_num = last_turn_num - turn_spoken[next_num]
		else:
			spoken_num = 0
		turn_spoken[next_num] = last_turn_num

		next_num = spoken_num
	
	return spoken_num

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument('-i', default='15', type=str, help='input file')
    args = parser.parse_args()

    with open(args.i, 'r') as f:
        data = [int(i.strip()) for i in f.read().split(',')]

        task1 = memory_game(data, 10)
        print(f"\nTask 1: {task1}")

        print(memory_game2(data, 2020))
        task2 = memory_game2(data, 30000000)
        print(f"\nTask 2: {task2}")
