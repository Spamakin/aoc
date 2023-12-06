from tqdm import tqdm

ss = list()
sf = list()
fw = list()
wl = list()
lt = list()
th = list()
hl = list()
seeds = list()
seed_ranges = list()

def parse_ranges(path):
    # get seeds
    with open(f"{path}/seeds.txt") as f:
        seed_s = f.readline()
        for num in seed_s.split():
            seeds.append(int(num))
        # print(seeds)


    # ss
    with open(f"{path}/ss.txt") as f:
        for line in f:
            line_s = line.split()
            nums = [int(i) for i in line_s]
            ss.append(nums)
        # print(ss)

    # sf
    with open(f"{path}/sf.txt") as f:
        for line in f:
            line_s = line.split()
            nums = [int(i) for i in line_s]
            sf.append(nums)
        # print(sf)

    # fw
    with open(f"{path}/fw.txt") as f:
        for line in f:
            line_s = line.split()
            nums = [int(i) for i in line_s]
            fw.append(nums)
        # print(fw)

    # wl
    with open(f"{path}/wl.txt") as f:
        for line in f:
            line_s = line.split()
            nums = [int(i) for i in line_s]
            wl.append(nums)
        # print(wl)

    # lt
    with open(f"{path}/lt.txt") as f:
        for line in f:
            line_s = line.split()
            nums = [int(i) for i in line_s]
            lt.append(nums)
        # print(lt)

    # th
    with open(f"{path}/th.txt") as f:
        for line in f:
            line_s = line.split()
            nums = [int(i) for i in line_s]
            th.append(nums)
        # print(th)

    # hl
    with open(f"{path}/hl.txt") as f:
        for line in f:
            line_s = line.split()
            nums = [int(i) for i in line_s]
            hl.append(nums)
        # print(hl)

def find_loc(seed):
    # ss
    soil = seed
    for d, s, r in ss:
        if s <= seed < s + r:
            soil = d + (seed - s)
            break

    # sf
    fert = soil
    for d, s, r in sf:
        if s <= soil < s + r:
            fert = d + (soil - s)
            break

    # fw
    water = fert
    for d, s, r in fw:
        if s <= fert < s + r:
            water = d + (fert - s)
            break

    # wl
    light = water
    for d, s, r in wl:
        if s <= water < s + r:
            light = d + (water - s)
            break

    # lt
    temp = light
    for d, s, r in lt:
        if s <= light < s + r:
            temp = d + (light - s)
            break

    # th
    hum = temp
    for d, s, r in th:
        if s <= temp < s + r:
            hum = d + (temp - s)
            break

    # hl
    loc = hum
    for d, s, r in hl:
        if s <= hum < s + r:
            loc = d + (hum - s)
            break

    # print(f"{seed}, {soil}, {fert}, {water}, {light}, {temp}, {hum}, {loc}")
    return loc

def find_seed(loc):
    # hl
    hum = loc
    for d, s, r in hl:
        if d <= loc < d + r:
            hum = s + (loc - d)
            break

    # th
    temp = hum
    for d, s, r in th:
        if d <= hum < d + r:
            temp = s + (hum - d)
            break

    # lt
    light = temp
    for d, s, r in lt:
        if d <= temp < d + r:
            light = s + (temp - d)
            break

    # wl
    water = light
    for d, s, r in wl:
        if d <= light < d + r:
            water = s + (light - d)
            break

    # fw
    fert = water
    for d, s, r in fw:
        if d <= water < d + r:
            fert = s + (water - d)
            break

    # sf
    soil = fert
    for d, s, r in sf:
        if d <= fert < d + r:
            soil = s + (fert - d)
            break
    # ss
    seed = soil
    for d, s, r in ss:
        if d <= soil < d + r:
            seed = s + (soil - d)
            break

    for (l, r) in seed_ranges:
        if l <= seed < l + r:
            # print(f"{loc}, {hum}, {temp}, {light}, {water}, {fert}, {soil}, {seed}")
            # print(f"{seed}, {soil}, {fert}, {water}, {light}, {temp}, {hum}, {loc}")
            return seed
    return -1

def main():
    path = "test"
    parse_ranges(path)
    min_loc = float("inf")
    for seed in seeds:
        loc = find_loc(seed)
        min_loc = min(min_loc, loc)
    print("part 1:", min_loc)

    # get seed_ranges [l, l + r)
    for (l, r) in zip(seeds[::2], seeds[1::2]):
        seed_ranges.append((l, r))

    max_loc = max(l + r for (l, r) in seed_ranges)
    print(max_loc)
    min_loc = float("inf")
    for loc in range(max_loc + 1):
        seed = find_seed(loc)
        if seed != -1:
            min_loc = min(min_loc, loc)
    print("part 2:", min_loc)

if __name__ == "__main__":
    main()
