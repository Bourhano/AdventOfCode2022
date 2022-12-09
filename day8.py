import numpy as np

with open('inputs/input8.txt', 'r') as f:
    a = f.read().strip().split('\n')

m, n = len(a), len(a[0])
full_map = np.zeros((m, n))
for i, line in enumerate(a):
    full_map[i] = list(line)

ans = 2 * (m + n - 2)
for i in range(1, m-1):
    for j in range(1, n-1):
        current = full_map - full_map[i, j]
        up = (current[:i, j] < 0).all()
        down = (current[i+1:, j] <  0).all()
        right = (current[i, j+1:] < 0).all()
        left = (current[i, :j] < 0).all()
        ans += left|right|up|down

print(ans)