pos = 50
count_zero = 0

with open("data.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        direction = line[0]          
        distance = int(line[1:])     

        if direction == 'L':
            pos = (pos - distance) % 100
        else:   # 'R'
            pos = (pos + distance) % 100

        if pos == 0:
            count_zero += 1

print("Password =", count_zero)
