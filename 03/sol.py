lines = []
with open("input.txt", "r") as f:
    for line in f:
        lines.append(line.strip())


def is_part(curr, line, i, j):
    forbidden = ".0123456789"
    for idx in range(i, j + 1):
        if idx > 0:
            if lines[curr][idx - 1] not in forbidden:
                return True
        if idx > 0 and curr > 0:
            if lines[curr - 1][idx - 1] not in forbidden:
                return True
        if curr > 0:
            if lines[curr - 1][idx] not in forbidden:
                return True
        if idx < len(line) - 1 and curr > 0:
            if lines[curr - 1][idx + 1] not in forbidden:
                return True
        if idx < len(line) - 1:
            if lines[curr][idx + 1] not in forbidden:
                return True
        if idx < len(line) - 1 and curr < len(lines) - 1:
            if lines[curr + 1][idx + 1] not in forbidden:
                return True
        if curr < len(lines) - 1:
            if lines[curr + 1][idx] not in forbidden:
                return True
        if idx > 0 and curr < len(lines) - 1:
            if lines[curr + 1][idx - 1] not in forbidden:
                return True
    return False


def find_nums(curr, line):
    digits = "0123456789"
    nums = []
    i = 0
    while i < len(line):
        if line[i] in digits:
            j = i
            while j < len(line) and line[j] in digits:
                j += 1

            if is_part(curr, line, i, j - 1):
                nums.append(int(line[i:j]))
            i = j - 1
        i += 1

    return sum(nums)


def is_gear(curr, line, i):
    digits = "0123456789"
    nums = []
    # left
    if i > 0 and line[i - 1] in digits:
        j = i - 1
        while j >= 0 and line[j] in digits:
            j -= 1
        print(line[j + 1 : i])
        if len(line[j + 1 : i]) > 0:
            nums.append(int(line[j + 1 : i]))
    # right
    if i < len(line) + 1 and line[i + 1] in digits:
        j = i + 1
        while j < len(line) and line[j] in digits:
            j += 1
        if len(line[i + 1 : j]) > 0:
            nums.append(int(line[i + 1 : j]))
    # top
    if curr > 0:
        l = i - 1
        while l > 0 and lines[curr - 1][l] in digits:
            l -= 1
        r = i + 1
        while r < len(lines[curr - 1]) and lines[curr - 1][r] in digits:
            r += 1
        s = lines[curr - 1][l:r]
        pot = s.split(".")
        filtered = []
        for p in pot:
            if len(p) > 0 and all(c in digits for c in p):
                filtered.append(p)
        for f in filtered:
            nums.append(int(f))
    # bottom
    if curr < len(lines) - 1:
        l = i - 1
        while l > 0 and lines[curr + 1][l] in digits:
            l -= 1
        r = i + 1
        while r < len(lines[curr + 1]) and lines[curr + 1][r] in digits:
            r += 1
        s = lines[curr + 1][l + 1 : r]
        pot = s.split(".")
        filtered = []
        for p in pot:
            if len(p) > 0 and all(c in digits for c in p):
                filtered.append(p)
        for f in filtered:
            nums.append(int(f))
    if curr > 0:
        print(lines[curr - 1])
    print(line)
    if curr < len(lines) - 1:
        print(lines[curr + 1])
    print(nums)
    print()

    if len(nums) == 2:
        return nums[0] * nums[1]
    else:
        return 0


def find_gears(curr, line):
    total = 0
    for i in range(len(line)):
        if line[i] == "*":
            total += is_gear(curr, line, i)
    return total


def main():
    # curr = 0
    # total = 0
    # for line in lines:
    #     total += find_nums(curr, line)
    #     curr += 1
    # print(total)

    curr = 0
    total = 0
    for line in lines:
        total += find_gears(curr, line)
        curr += 1
    print(total)


if __name__ == "__main__":
    main()
