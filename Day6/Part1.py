def solve():
    # Read entire worksheet as grid of characters
    with open("data.txt") as f:
        lines = [line.rstrip("\n") for line in f]

    # Normalize the grid so all rows have equal width
    width = max(len(line) for line in lines)
    grid = [line.ljust(width) for line in lines]

    problems = []
    col = 0

    while col < width:
        # Skip columns of only spaces (separators)
        if all(row[col] == " " for row in grid):
            col += 1
            continue

        # Collect contiguous non-space columns → one problem block
        start = col
        while col < width and not all(row[col] == " " for row in grid):
            col += 1
        end = col  # non-inclusive

        # Extract the block
        block = [row[start:end] for row in grid]

        # Find the operation — last non-empty row in the block
        op_row = None
        for r in range(len(block) - 1, -1, -1):
            if any(c in "+*" for c in block[r]):
                op_row = r
                break
        operation = "+" if "+" in block[op_row] else "*"

        # Extract numbers (any row above the operation row)
        numbers = []
        for r in range(op_row):
            stripped = block[r].strip()
            if stripped.isdigit():
                numbers.append(int(stripped))

        # Compute result of this problem
        if operation == "+":
            value = sum(numbers)
        else:  # multiplication
            value = 1
            for x in numbers:
                value *= x

        problems.append(value)

    print("Grand total:", sum(problems))


if __name__ == "__main__":
    solve()
