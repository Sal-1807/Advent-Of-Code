def max_12_digit_number(bank, k=12):
    stack = []
    remove = len(bank) - k  

    for digit in bank:
        while remove > 0 and stack and stack[-1] < digit:
            stack.pop()
            remove -= 1
        stack.append(digit)

    return int("".join(stack[:k]))


total = 0

with open("data.txt") as f:
    for line in f:
        bank = line.strip()
        total += max_12_digit_number(bank, 12)

print("Total output joltage ", total)
