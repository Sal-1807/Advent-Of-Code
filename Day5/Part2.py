def count_all_fresh_ids(filename="data.txt"):
    ranges = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line == "":
                break
            a, b = map(int, line.split("-"))
            ranges.append((a, b))

    ranges.sort()

    merged = []
    cur_start, cur_end = ranges[0]

    for s, e in ranges[1:]:
        if s <= cur_end + 1:
            cur_end = max(cur_end, e)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = s, e

    merged.append((cur_start, cur_end))

    total = 0
    for a, b in merged:
        total += (b - a + 1)

    return total


print(count_all_fresh_ids("data.txt"))
