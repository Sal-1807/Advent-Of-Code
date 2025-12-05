def count_fresh(filename="data.txt"):
    lines = [line.strip() for line in open(filename) if line.strip() != ""]

    # Split into ranges section and id list section.
    # Find the first non-range line → that's where IDs start.
    ranges = []
    ids = []

    # Ranges contain '-', IDs don't.
    for line in lines:
        if "-" in line:
            a, b = map(int, line.split("-"))
            ranges.append((a, b))
        else:
            ids.append(int(line))

    fresh_count = 0

    for x in ids:
        for a, b in ranges:
            if a <= x <= b:
                fresh_count += 1
                break  # no need to check other ranges

    return fresh_count


print(count_fresh("data.txt"))
