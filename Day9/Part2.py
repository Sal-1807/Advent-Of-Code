with open("data.txt") as f:
    red = [tuple(map(int, line.split(","))) for line in f]

# --- coordinate compression ---
class CC:
    def __init__(self, vals):
        import random
        r = random.getrandbits(32)
        self.r = r
        self.orig = []
        self.map = {}
        for v in sorted(vals):
            if not self.orig or v != self.orig[-1]:
                self.orig.append(v)
                self.map[v ^ r] = len(self.map)

    def c(self, v):
        return self.map[v ^ self.r]

    def o(self, i):
        return self.orig[i]

xs, ys = set(), set()
for x, y in red:
    xs |= {x-1, x, x+1}
    ys |= {y-1, y, y+1}

cx, cy = CC(xs), CC(ys)
red_c = [(cx.c(x), cy.c(y)) for x, y in red]

# --- fill inside region ---
inside = set()

# trace boundary
n = len(red_c)
for i in range(n):
    x1, y1 = red_c[i]
    x2, y2 = red_c[(i+1) % n]
    for X in range(min(x1, x2), max(x1, x2)+1):
        for Y in range(min(y1, y2), max(y1, y2)+1):
            inside.add((X, Y))

# flood fill interior
xm = max(x for x, _ in red_c)
i = next(k for k,(X,_) in enumerate(red_c) if X == xm)
j = (i+1) % n if red_c[(i+1) % n][0] == xm else (i-1) % n
seed = (red_c[i][0]-1, red_c[i][1] + (1 if red_c[i][1] < red_c[j][1] else -1))

queue = [seed]
inside.add(seed)
for x, y in queue:
    for nx, ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
        if (nx, ny) not in inside:
            inside.add((nx, ny))
            queue.append((nx, ny))

# --- border check ---
def ok(x1, y1, x2, y2):
    for y in range(min(y1,y2), max(y1,y2)+1):
        if (x1,y) not in inside or (x2,y) not in inside:
            return False
    for x in range(min(x1,x2), max(x1,x2)+1):
        if (x,y1) not in inside or (x,y2) not in inside:
            return False
    return True

# --- compute part 2 ---
best = 0
for i in range(n):
    x1,y1 = red_c[i]
    for j in range(i+1, n):
        x2,y2 = red_c[j]
        if ok(x1,y1,x2,y2):
            dx = abs(cx.o(x2) - cx.o(x1))
            dy = abs(cy.o(y2) - cy.o(y1))
            best = max(best, (dx+1)*(dy+1))

print(best)
