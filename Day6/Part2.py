def solve():
    with open("data.txt") as f:
        rows = [line.rstrip("\n") for line in f]
    
    W = max(len(r) for r in rows)
    grid = [r.ljust(W) for r in rows]
    H = len(grid)

    problems = []
    col = W - 1     

    while col >= 0:
        if all(grid[r][col] == " " for r in range(H)):
            col -= 1
            continue

        end = col
        while col >= 0 and not all(grid[r][col] == " " for r in range(H)):
            col -= 1
        start = col + 1

        block = [grid[r][start:end+1] for r in range(H)]

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

        numbers = []
        for c in range(len(block[0])):        
            digits = []
            for r in range(op_row):           
                ch = block[r][c]
                if ch.isdigit():
                    digits.append(ch)
            if digits:
                num = int("".join(digits))
                numbers.append(num)

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
