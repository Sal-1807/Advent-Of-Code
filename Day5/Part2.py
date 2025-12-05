def count_all_fresh_ids(filename="data.txt"):
    # Read ranges only (stop at blank line)
    ranges = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line == "":
                break
            a, b = map(int, line.split("-"))
            ranges.append((a, b))

    # Sort ranges by starting point
    ranges.sort()

    # Merge overlapping intervals
    merged = []
    cur_start, cur_end = ranges[0]

    for s, e in ranges[1:]:
        if s <= cur_end + 1:
            # Overlaps or touches -> extend
            cur_end = max(cur_end, e)
        else:
            # No overlap -> push interval
            merged.append((cur_start, cur_end))
            cur_start, cur_end = s, e

    merged.append((cur_start, cur_end))

    # Count size of merged intervals
    total = 0
    for a, b in merged:
        total += (b - a + 1)

    return total


print(count_all_fresh_ids("data.txt"))
