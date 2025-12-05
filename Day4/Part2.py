def total_removed(filename="data.txt"):
    grid = [list(line.strip()) for line in open(filename)]
    R, C = len(grid), len(grid[0])

    dirs = [
        (-1,-1), (-1,0), (-1,1),
        (0,-1),          (0,1),
        (1,-1), (1,0), (1,1)
    ]

    total = 0

    while True:
        to_remove = []

        # Find all accessible @ rolls
        for r in range(R):
            for c in range(C):
                if grid[r][c] != '@':
                    continue

                adj = 0
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < R and 0 <= nc < C:
                        if grid[nr][nc] == '@':
                            adj += 1

                if adj < 4:
                    to_remove.append((r, c))

        # If none found, stop
        if not to_remove:
            break

        # Remove them
        for r, c in to_remove:
            grid[r][c] = '.'

        total += len(to_remove)

    return total


print(total_removed("data.txt"))
