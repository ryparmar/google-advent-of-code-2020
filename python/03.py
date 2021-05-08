import argparse
import math

# Python 3.8 needed as the math.prod is not in previous versions
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument('-i', type=str, help='input file')
    args = parser.parse_args()

    with open(args.i, 'r') as f:
        data = [str(line).strip('\n') for line in f]
        
        # Task 1
        slope_h, slope_v = 3, 1
        trees = 0
        h = 0  # horizontal coordinate
        # print(len(data[0]))
        for i in range(0, len(data), slope_v):  # i = vertical coordinate
            # print(i, h, data[i][h])
            if data[i][h] == '#':
                trees += 1
            h = (h + slope_h) - len(data[0]) if (h + slope_h) >= len(data[0]) else h + slope_h


        # Task 2
        slopes_h, slopes_v = [1, 3, 5, 7, 1], [1, 1, 1, 1, 2]
        trees2 = [0] * len(slopes_h)
        for ii, (slope_h, slope_v) in enumerate(zip(slopes_h, slopes_v)):
            h = 0
            for i in range(0, len(data), slope_v):  # i = vertical coordinate
                if data[i][h] == '#':
                    trees2[ii] += 1
                h = (h + slope_h) - len(data[0]) if (h + slope_h) >= len(data[0]) else h + slope_h

        print(f"Task 1: Trees encountered: {trees}")
        print(f"Task 2: Trees encountered: {trees2} with multiplication of them: {math.prod(trees2)}")