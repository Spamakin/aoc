def process_seq(seq):
    curr = seq
    seqns = [seq]
    while not all(x == 0 for x in curr):
        assert len(curr) >= 2
        total = curr[-1] + (curr[-1] - curr[-2])
        diffs = []
        for i in range(len(curr) - 1):
            diffs.append(curr[i + 1] - curr[i])
        seqns.append(diffs)
        curr = diffs

    f = 0
    b = 0
    for curr in reversed(seqns):
        f = f + curr[-1]
        b = curr[0] - b

    return f, b


def main():
    path = "input.txt"

    ftotal = 0
    btotal = 0
    with open(path, "r") as f:
        for line in f:
            seq = []
            for num in line.strip().split():
                seq.append(int(num))
            f, b = process_seq(seq)
            ftotal += f
            btotal += b
    print(ftotal)
    print(btotal)


if __name__ == "__main__":
    main()
