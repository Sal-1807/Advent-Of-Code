TEST = 0
import collections
from z3 import Solver, Int, solve, Optimize

path = "data.txt"
if TEST:
    path = path.replace("real", "test")

file = open(path)
ret = 0
coords = []

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]


for line in file.readlines():
    parts = line.strip().split(' ')
    lights = parts[0]
    wiring = parts[1:-1]
    joltage = parts[-1]
    lights = [x == '#' for x in lights[1:-1]]
    n = len(lights)
    start = []
    for i in range(n):
        if lights[i]:
            start.append(i)

    def to_multmask(x):
        y = 1
        for i in x:
            y *= primes[i]
        return y

    def from_bitmask(x):
        y = []
        for i in range(n):
            if x % 2 == 1:
                y.append(i)
            x //= 2
        return y

    buttons = [[int(x) for x in wire[1:-1].split(',')] for wire in wiring]

    start = 0
    # buttons = [to_multmask(x) for x in buttons]
    # end = to_bitmask(list(range(n)))
    end = [int(num) for num in joltage[1:-1].strip().split(',')]

    presses = Int('presses')
    counters = [Int('count' + str(i)) for i in range(len(end))]
    button_vars = [Int('button' + str(i)) for i in range(len(buttons))]

    counters_to_buttons = collections.defaultdict(list)
    for i, button in enumerate(buttons):
        for flip in button:
            counters_to_buttons[flip].append(i)

    equations = []
    for counter, counter_buttons in counters_to_buttons.items():
        # equations.append(counters[counter] == sum([button_vars[i] for i in counter_buttons]))
        equations.append(end[counter] == sum([button_vars[i] for i in counter_buttons]))
    # for i in range(len(end)):
    #     equations.append()
    for button_var in button_vars:
        equations.append(button_var >= 0)
    equations.append(presses == sum(button_vars))
    # print(equations)
    # print(solve(equations))
    # print(presses)
    opt = Optimize()
    opt.add(equations)
    # print()
    # print(opt)
    opt.minimize(presses)
    opt.check()
    output = opt.model()[presses]
    print(output)
    ret += int(str(output))

print(ret)
