import numpy as np

with open('inputs/inputx10.txt', 'r') as f:
    a = f.read().strip().split('\n')

cycle = 1
cycles = np.array([20, 60, 100, 140, 180, 220]) + 20
X = 1
ans = ""
ans += "#" if cycle in [X-1, X, X+1] else '.'
for line in a:
    cmd = line.split()

    cycle += 1
    ans += "#" if (cycle-1)%40 in [X-1, X, X+1] else '.'
    if cmd[0] == 'addx':
        if cycle in cycles:
            ans += "\n"
        cycle += 1
        X += int(cmd[1])
        ans += "#" if (cycle-1)%40 in [X-1, X, X+1] else '.'

    if cycle in cycles:
        ans += "\n"

print(ans)
