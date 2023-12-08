with open("input.txt", "r") as f:
    # Part 1
    total = 0
    for line in f:
        num = 0
        for c in line:
            if ord("0") <= ord(c) <= ord("9"):
                num = int(c)
                break
        for c in reversed(line):
            if ord("0") <= ord(c) <= ord("9"):
                num = 10 * num + int(c)
                break

        total += int(num)

    print(total)

with open("input.txt", "r") as f:
    # Part 2
    total = 0
    words = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for line in f:
        num = 0
        curr = 0
        curr_idx = float("inf")
        for i, token in enumerate(words):
            idx = line.find(token)
            if idx != -1 and idx < curr_idx:
                curr_idx = idx
                curr = i
        for i, token in enumerate(nums):
            idx = line.find(token)
            if idx != -1 and idx < curr_idx:
                curr_idx = idx
                curr = i
        num += curr

        curr = 0
        curr_idx = float("-inf")
        for i, token in enumerate(words):
            idx = line.rfind(token)
            if idx != -1 and idx > curr_idx:
                curr_idx = idx
                curr = i
        for i, token in enumerate(nums):
            idx = line.rfind(token)
            if idx != -1 and idx > curr_idx:
                curr_idx = idx
                curr = i

        num = 10 * num + curr
        total += num

    print(total)
