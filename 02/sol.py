def process_round(line):
    line = line.strip()
    id_str, rounds = line.split(": ")

    # get id
    id_str = id_str[5:]
    id = int(id_str)

    # parse rounds into array
    rounds_arr = rounds.split("; ")
    game = []
    for handfuls in rounds_arr:
        r, g, b = 0, 0, 0
        colors = handfuls.split(", ")
        for color in colors:
            if "red" in color:
                r_str = color[:-4]
                r = int(r_str)
            if "green" in color:
                g_str = color[:-6]
                g = int(g_str)
            if "blue" in color:
                b_str = color[:-5]
                b = int(b_str)
        rgb = [r, g, b]
        game.append(rgb)

    return id, game


def is_possible(game):
    for handful in game:
        r, g, b = handful
        if r > 12:
            return False
        if g > 13:
            return False
        if b > 14:
            return False

    return True


def power(game):
    r_min, g_min, b_min = 0, 0, 0
    for handful in game:
        r, g, b = handful
        r_min = max(r_min, r)
        g_min = max(g_min, g)
        b_min = max(b_min, b)

    return r_min * g_min * b_min


def main():
    with open("input.txt", "r") as f:
        total = 0
        for line in f:
            id, game = process_round(line)
            if is_possible(game):
                total += id

        print(total)

    with open("input.txt", "r") as f:
        total = 0
        for line in f:
            _, game = process_round(line)
            total += power(game)

        print(total)


if __name__ == "__main__":
    main()
