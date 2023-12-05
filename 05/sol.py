from tqdm import tqdm

ss = list()
sf = list()
fw = list()
wl = list()
lt = list()
th = list()
hl = list()
seeds = set()
range_seeds = set()

def parse_ranges(path):
    # get seeds
    with open(f"{path}/seeds.txt") as f:
        seed_s = f.readline()
        nums = [int(num) for num in seed_s.split()]
        for num in nums:
            seeds.add(num)
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

def main():
    parse_ranges("input")
    # min_loc = float("inf")
    # for seed in seeds:
    #     loc = find_loc(seed)
    #     min_loc = min(min_loc, loc)
    # print(min_loc)

    # get seed_ranges
    min_loc = float("inf")
    with open(f"input/seeds.txt") as f:
        seed_s = f.readline()
        nums = [int(num) for num in seed_s.split()]
        for i in range(0, len(nums), 2):
            for seed in tqdm(range(nums[i], nums[i] + nums[i + 1])):
                loc = find_loc(seed)
                min_loc = min(min_loc, loc)
            print(min_loc)

if __name__ == "__main__":
    main()
