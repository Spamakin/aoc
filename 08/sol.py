from collections import defaultdict
from math import lcm


def main():
    path = "input.txt"
    test_moves = "LR"
    input_moves = "LRRRLRRLRRLRRLLLRRRLRRLLRRRLRLLLRRLRLRLRLRLRLRLRRRLLLRRLRRRLRLLRRRLRRRLRRRLLRRRLRLRRRLRRLRRRLLRLLRLLRRRLRRRLRRLRLRLLRLRRLRRRLRRRLRLRLRLRRLRLRLLLRRRLRLRLRRRLRRRLRRRLRLLLRRLRLRLRLRLLLRRRLRRLRRLRLRLRRRLRLRRRLRRRLRRRLRLRRRLLLRRLRRRLRRLLRLRRLRRLRRRLLLRRLRRLRRLRLRRRLLLRLRRRR"

    order = input_moves
    moves = dict()
    with open(path, "r") as f:
        for line in f:
            line_s = line.strip().split(" = ")
            moves[line_s[0]] = [line_s[1][1:4], line_s[1][6:9]]

    # # part 1
    # count = 0
    # curr = "AAA"
    # n = len(order)
    # while curr != "ZZZ":
    #     if order[count % n] == "L":
    #         curr = moves[curr][0]
    #     elif order[count % n] == "R":
    #         curr = moves[curr][1]
    #     count += 1
    # print(count)

    # part 2

    # init
    starts = []
    for k, v in moves.items():
        if k[2] == "A":
            starts.append(k)

    lengths = []
    for start in starts:
        count = 0
        curr = start
        n = len(order)
        while curr[2] != "Z":
            if order[count % n] == "L":
                curr = moves[curr][0]
            elif order[count % n] == "R":
                curr = moves[curr][1]
            count += 1
        lengths.append(count)

    print(lcm(*lengths))


if __name__ == "__main__":
    main()
