from itertools import combinations
import os

# ---------- Union–Find (Disjoint Set) ----------
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    def find(self, a):
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True
    def component_sizes(self):
        roots = {}
        for i in range(len(self.parent)):
            r = self.find(i)
            roots[r] = roots.get(r, 0) + 1
        return list(roots.values())

# ---------- Helpers ----------
def parse_points(lines):
    pts = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        x, y, z = map(int, line.split(','))
        pts.append((x, y, z))
    return pts

def squared_dist(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2

# ---------- Core solve function ----------
def solve(filename="data.txt", K=1000):
    if not os.path.exists(filename):
        print("data.txt not found")
        return

    with open(filename) as f:
        pts = parse_points(f.readlines())

    n = len(pts)
    uf = UnionFind(n)

    # Build all pairwise distances
    pairs = []
    for (i, a), (j, b) in combinations(enumerate(pts), 2):
        pairs.append((squared_dist(a, b), i, j))

    # Sort by shortest first
    pairs.sort(key=lambda x: x[0])

    # Process the K nearest pairs
    for dist, i, j in pairs[:K]:
        uf.union(i, j)

    sizes = sorted(uf.component_sizes(), reverse=True)

    # product of 3 largest
    ans = sizes[0] * sizes[1] * sizes[2]
    print(ans)

# Run on data.txt automatically
solve("data.txt", 1000)
