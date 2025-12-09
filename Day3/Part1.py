total = 0

with open("data.txt") as f:
    for line in f:
        bank = line.strip()
        best = 0

        for i in range(len(bank)):
            for j in range(i + 1, len(bank)):
                val = int(bank[i] + bank[j])  
                if val > best:
                    best = val

        total += best

print("Total output joltage =", total)
