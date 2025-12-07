def solve():
    # Read worksheet
    with open("data.txt") as f:
        rows = [line.rstrip("\n") for line in f]

    # Normalize rows to equal width
    W = max(len(r) for r in rows)
    grid = [r.ljust(W) for r in rows]
    H = len(grid)

    problems = []
    col = W - 1     # start RIGHT and move left

    while col >= 0:
        # skip separator columns (all spaces)
        if all(grid[r][col] == " " for r in range(H)):
            col -= 1
            continue

        # collect contiguous non-blank columns (a problem)
        end = col
        while col >= 0 and not all(grid[r][col] == " " for r in range(H)):
            col -= 1
        start = col + 1

        # extract the block (columns start..end inclusive)
        block = [grid[r][start:end+1] for r in range(H)]

        # find operation row
        op_row = None
        for r in range(H-1, -1, -1):
            if "+" in block[r]:
                op = "+"
                op_row = r
                break
            if "*" in block[r]:
                op = "*"
                op_row = r
                break

        # each COLUMN (not row!) above op_row is one number
        numbers = []
        for c in range(len(block[0])):        # each column in the block
            digits = []
            for r in range(op_row):           # collect digits ABOVE op row
                ch = block[r][c]
                if ch.isdigit():
                    digits.append(ch)
            if digits:
                num = int("".join(digits))
                numbers.append(num)

        # compute problem result
        if op == "+":
            val = sum(numbers)
        else:
            val = 1
            for x in numbers:
                val *= x

        problems.append(val)

    print("Grand total:", sum(problems))


if __name__ == "__main__":
    solve()
