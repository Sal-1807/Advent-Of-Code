# Advent-style puzzle: forklift-accessible rolls

def count_accessible(filename="data.txt"):
    grid = [list(line.strip()) for line in open(filename)]
    R, C = len(grid), len(grid[0])

    # 8-direction offsets
    dirs = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    accessible = 0

    for r in range(R):
        for c in range(C):
            if grid[r][c] != '@':
                continue

            count_adj = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C:
                    if grid[nr][nc] == '@':
                        count_adj += 1

            if count_adj < 4:
                accessible += 1

    return accessible


print(count_accessible("data.txt"))
