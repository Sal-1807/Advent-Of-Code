def solve():
    with open("data.txt") as f:
        lines = [line.rstrip("\n") for line in f]

    width = max(len(line) for line in lines)
    grid = [line.ljust(width) for line in lines]

    problems = []
    col = 0

    while col < width:
        if all(row[col] == " " for row in grid):
            col += 1
            continue

        start = col
        while col < width and not all(row[col] == " " for row in grid):
            col += 1
        end = col  

        block = [row[start:end] for row in grid]

        op_row = None
        for r in range(len(block) - 1, -1, -1):
            if any(c in "+*" for c in block[r]):
                op_row = r
                break
        operation = "+" if "+" in block[op_row] else "*"

        numbers = []
        for r in range(op_row):
            stripped = block[r].strip()
            if stripped.isdigit():
                numbers.append(int(stripped))

        if operation == "+":
            value = sum(numbers)
        else:  
            value = 1
            for x in numbers:
                value *= x

        problems.append(value)

    print("Grand total:", sum(problems))


if __name__ == "__main__":
    solve()
