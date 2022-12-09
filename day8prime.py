import numpy as np

with open('inputs/input8.txt', 'r') as f:
    a = f.read().strip().split('\n')

m, n = len(a), len(a[0])
full_map = np.zeros((m, n))
for i, line in enumerate(a):
    full_map[i] = list(line)

best = -1
for i in range(1, m-1):
    for j in range(1, n-1):
        score_up, score_down, score_left, score_right = 0, 0, 0, 0
        current = full_map - full_map[i, j]

        up = current[:i, j][::-1]
        for el in up:
            score_up += 1
            if el >= 0:
                break

        down = current[i+1:, j]
        for el in down:
            score_down += 1
            if el >= 0:
                break
        
        right = current[i, j+1:]
        for el in right:
            score_right += 1
            if el >= 0:
                break

        left = current[i, :j][::-1]
        for el in left:
            score_left += 1
            if el >= 0:
                break

        score = score_up * score_down * score_right * score_left

        if score > best:
            best = score

print(best)
