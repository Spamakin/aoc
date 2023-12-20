from collections import defaultdict
from functools import cmp_to_key

cards1 = "23456789TJQKA"
cards2 = "J23456789TQKA"


# High = 0
# One = 1
# Two = 2
# Three = 3
# Full = 4
# Four = 5
# Five = 6
def hand_type1(H):
    counts = defaultdict(int)
    for c in H:
        counts[c] += 1
    labels = []
    for _, v in counts.items():
        labels.append(v)
    labels = list(sorted(labels))

    # Five of a Kind
    if labels == [5]:
        return 6
    # Four of a Kind
    if labels == [1, 4]:
        return 5
    # Full House
    if labels == [2, 3]:
        return 4
    # Three of a Kind
    if labels == [1, 1, 3]:
        return 3
    # Two Pair
    if labels == [1, 2, 2]:
        return 2
    # One Pair
    if labels == [1, 1, 1, 2]:
        return 1
    # High
    if labels == [1, 1, 1, 1, 1]:
        return 0


def compare_hands1(H1, H2):
    if hand_type1(H1) == hand_type1(H2):
        for c1, c2 in zip(H1, H2):
            if cards1.index(c1) > cards1.index(c2):
                return 1
            elif cards1.index(c1) < cards1.index(c2):
                return -1
        return 0
    return hand_type1(H1) - hand_type1(H2)


def compare_pairs1(HB1, HB2):
    return compare_hands1(HB1[0], HB2[0])


# High = 0
# One = 1
# Two = 2
# Three = 3
# Full = 4
# Four = 5
# Five = 6
def hand_type2(H):
    if "J" not in H:
        return hand_type1(H)
    # So have Jokers!
    Jcount = H.count("J")

    counts = defaultdict(int)
    for c in H:
        if c != "J":
            counts[c] += 1

    # Most efficient use of Jokers is most common card
    most_common_k = None
    most_common_v = 0
    for k, v in counts.items():
        if v > most_common_v:
            most_common_v = v
            most_common_k = k
    counts[most_common_k] += Jcount
    labels = []
    for _, v in counts.items():
        labels.append(v)
    labels = list(sorted(labels))

    # Five of a Kind
    if labels == [5]:
        return 6
    # Four of a Kind
    if labels == [1, 4]:
        return 5
    # Full House
    if labels == [2, 3]:
        return 4
    # Three of a Kind
    if labels == [1, 1, 3]:
        return 3
    # Two Pair
    if labels == [1, 2, 2]:
        return 2
    # One Pair
    if labels == [1, 1, 1, 2]:
        return 1
    # High
    if labels == [1, 1, 1, 1, 1]:
        return 0


def compare_hands2(H1, H2):
    if hand_type2(H1) == hand_type2(H2):
        for c1, c2 in zip(H1, H2):
            if cards2.index(c1) > cards2.index(c2):
                return 1
            elif cards2.index(c1) < cards2.index(c2):
                return -1
        return 0
    return hand_type2(H1) - hand_type2(H2)


def compare_pairs2(HB1, HB2):
    return compare_hands2(HB1[0], HB2[0])


def main():
    path = "input.txt"
    HB = []
    with open(path, "r") as f:
        for line in f:
            hb = line.strip().split()
            H = [c for c in hb[0]]
            B = int(hb[1])
            HB.append([H, B])

    # part 1
    HBs = sorted(HB, key=cmp_to_key(compare_pairs1))
    winnings = 0
    for i, (_, B) in enumerate(HBs):
        winnings += (i + 1) * B
    print("part 1:", winnings)

    # part 2
    HBs = sorted(HB, key=cmp_to_key(compare_pairs2))
    winnings = 0
    for i, (_, B) in enumerate(HBs):
        winnings += (i + 1) * B
    print("part 2:", winnings)


if __name__ == "__main__":
    main()
