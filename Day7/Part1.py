from collections import deque

def count_splits(filename="data.txt"):
    # Read file and build a rectangular grid (pad rows with spaces)
    with open(filename, "r") as f:
        rows = [line.rstrip("\n") for line in f]
    if not rows:
        return 0

    W = max(len(r) for r in rows)
    grid = [r.ljust(W) for r in rows]
    H = len(grid)

    # find S
    start_r = start_c = None
    for r in range(H):
        c = grid[r].find("S")
        if c != -1:
            start_r, start_c = r, c
            break
    if start_r is None:
        raise ValueError("No starting 'S' found in input")

    # initial beam starts immediately below S
    start_pos = (start_r + 1, start_c)

    # BFS/DFS over beam positions; each (r,c) is a beam head location to process
    q = deque()
    visited = set()
    if 0 <= start_pos[0] < H:
        q.append(start_pos)
        visited.add(start_pos)

    splits = 0

    while q:
        r, c = q.popleft()

        # if beam has fallen out of the grid, ignore
        if r >= H or c < 0 or c >= W:
            continue

        ch = grid[r][c]

        # If we hit a splitter
        if ch == "^":
            splits += 1
            # spawn beams at immediate left and right (same row)
            for nc in (c - 1, c + 1):
                np = (r, nc)
                if 0 <= nc < W and np not in visited:
                    visited.add(np)
                    q.append(np)
        else:
            # treat anything other than '^' as empty/pass-through ('.', 'S', space, etc.)
            # beam continues downward
            np = (r + 1, c)
            if np not in visited and np[0] < H:
                visited.add(np)
                q.append(np)

    return splits

if __name__ == "__main__":
    print(count_splits("data.txt"))
