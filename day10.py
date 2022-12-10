with open('inputs/inputx10.txt', 'r') as f:
    a = f.read().strip().split('\n')

cycle = 1
cycles = [20, 60, 100, 140, 180, 220]
X = 1
ans = 0
for line in a:
    cmd = line.split()

    cycle += 1
    if cmd[0] == 'addx':
        if cycle in cycles:
            ans += X * cycle
        cycle += 1
        X += int(cmd[1])

    if cycle in cycles:
        ans += X * cycle


print(ans)
