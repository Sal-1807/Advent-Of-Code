total = 0

with open("data.txt") as f:
    for line in f:
        bank = line.strip()
        best = 0

        # consider every possible pair of positions i < j
        for i in range(len(bank)):
            for j in range(i + 1, len(bank)):
                val = int(bank[i] + bank[j])  # two-digit number
                if val > best:
                    best = val

        total += best

print("Total output joltage =", total)
