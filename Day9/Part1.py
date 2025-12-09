from itertools import combinations

pts = []
with open("data.txt") as f:
    for line in f:
        x, y = map(int, line.strip().split(","))
        pts.append((x, y))

max_area = 0

for (x1, y1), (x2, y2) in combinations(pts, 2):
    area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
    if area > max_area:
        max_area = area

print(max_area)
