def main():
    path = "input.txt"
    times, dists = [], []
    with open(path, "r") as f:
        time_s = f.readline().split(":")[1].strip().split()
        for time in time_s:
            times.append(int(time))

        dist_s = f.readline().split(":")[1].strip().split()
        for dist in dist_s:
            dists.append(int(dist))

    total = 1
    for time, dist in zip(times, dists):
        count = 0
        for hold in range(1, time):
            speed = hold
            travel_time = time - hold
            if speed * travel_time > dist:
                count += 1
        total *= count
    print(total)

    path = "input.txt"
    times, dists = "", ""
    with open(path, "r") as f:
        time_s = f.readline().split(":")[1].strip().split()
        for time in time_s:
            times += time

        dist_s = f.readline().split(":")[1].strip().split()
        for dist in dist_s:
            dists += dist
    times = int(times)
    dists = int(dists)

    count = 0
    for hold in range(1, times):
        speed = hold
        travel_time = times - hold
        if speed * travel_time > dists:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
