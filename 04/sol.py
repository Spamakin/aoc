from collections import defaultdict

mult = defaultdict(int)

def score(win, have):
    n = 0
    for card in have:
        n += win.count(card)

    if n == 0:
        return 0, 0
    else:
        return 2**(n-1), n

def parse(line):
    cards = line.split(": ")[1]
    both = cards.split(" | ")
    win_s = both[0].split()
    have_s = both[1].split()
    win = [int(num) for num in win_s]
    have = [int(num) for num in have_s]

    return win, have

def main():
    with open("input.txt", "r") as f:
        total = 0
        copies = 0
        curr = 1
        for line in f:
            line = line.strip()
            win, have = parse(line)
            won, count = score(win, have)
            mult[curr] += 1
            for i in range(curr + 1, curr + count + 1):
                mult[i] += mult[curr]
            total += won
            copies += mult[curr]
            curr += 1
        print(total)
        print(copies)



if __name__ == "__main__":
    main()
