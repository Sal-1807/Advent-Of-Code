def count_fresh(filename="data.txt"):
    lines = [line.strip() for line in open(filename) if line.strip() != ""]

    ranges = []
    ids = []

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
                break  
    return fresh_count


print(count_fresh("data.txt"))
