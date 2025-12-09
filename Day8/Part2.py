#!/usr/bin/env python3
from itertools import combinations
import os
import sys

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
        self.count = n  # number of components
    def find(self, a):
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a
    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.count -= 1
        return True

def parse_points(lines):
    pts = []
    for line in lines:
        s = line.strip()
        if not s:
            continue
        x,y,z = map(int, s.split(','))
        pts.append((x,y,z))
    return pts

def squared_dist(a,b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2

def main(filename="data.txt"):
    if not os.path.exists(filename):
        print("data.txt not found", file=sys.stderr)
        sys.exit(1)

    with open(filename, 'r') as f:
        pts = parse_points(f.readlines())

    n = len(pts)
    if n == 0:
        print("no points", file=sys.stderr)
        sys.exit(1)
    if n == 1:
        print(pts[0][0]*pts[0][0])  # trivial
        return

    # Build all pairwise distances
    pairs = []
    for (i,a),(j,b) in combinations(list(enumerate(pts)), 2):
        pairs.append((squared_dist(a,b), i, j))

    pairs.sort(key=lambda x: x[0])

    uf = UnionFind(n)

    for dist, i, j in pairs:
        merged = uf.union(i, j)
        if merged and uf.count == 1:
            # Found the connection that makes everything a single component
            x_prod = pts[i][0] * pts[j][0]
            print(x_prod)
            return

    # If loop finishes without count==1, the input was already all connected? handle:
    print("All points were not connected by the processed pairs.", file=sys.stderr)
    sys.exit(1)

if __name__ == "__main__":
    # optionally take filename from argv
    fname = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    main(fname)
