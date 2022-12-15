import numpy as np
from time import sleep

with open('inputs/inputx14.txt', 'r') as f:
    a = f.read().strip().split('\n')

minx, maxx, miny, maxy = 1000, 0, 1000, 0
elements = []
for line in a:
    coords = line.split(' -> ')
    blocks = []
    for block in [coord.split(',') for coord in coords]:
        x, y = block[0], block[1]
        x, y = int(x), int(y)
        blocks.append((y, x))
        if x > maxx:
            maxx = x
        if x < minx:
            minx = x
        if y > maxy:
            maxy = y
        if y < miny:
            miny = y
    elements.append(blocks)

MARGIN = 3

grid = np.zeros((maxy + MARGIN, maxx - minx + MARGIN*2))
print(minx, maxx, miny, maxy)
print(grid.shape)

for el in elements:
    for i in range(1, len(el)):
        if el[i][0] == el[i-1][0]:  # y constant
            if el[i][1] < el[i-1][1]:
                grid[el[i][0], el[i][1] - minx + MARGIN: el[i-1][1] - minx + MARGIN +1] = [1] * abs(el[i][1] - el[i-1][1] -1)
            else:
                grid[el[i][0], el[i-1][1] - minx + MARGIN: el[i][1] - minx + MARGIN +1] = [1] * abs(el[i][1] - el[i-1][1] +1)
        elif el[i][1] == el[i-1][1]:  # x constant
            if el[i][0] < el[i-1][0]:
                # print(len(grid[el[i][0]:el[i-1][0]+1, el[i][1] - minx + MARGIN]))
                # print(len([1] * abs(el[i][0] - el[i-1][0] -1)))
                # print()
                # print(el[i][0], el[i-1][0]+1, el[i][1] - minx + MARGIN,)
                grid[el[i][0]:el[i-1][0]+1, el[i][1] - minx + MARGIN] = [1] * abs(el[i][0] - el[i-1][0] -1)
            else:
                grid[el[i-1][0]:el[i][0]+1, el[i][1] - minx + MARGIN] = [1] * abs(el[i][0] - el[i-1][0] +1)

init_sand = (0, 500 - minx + MARGIN)
grid[init_sand] = -1

current_sand = init_sand
ans = 0

while sum(grid[current_sand[0]:, current_sand[1]]) > -1:
    # print(grid[current_sand[0], current_sand[1]:])
    # print(grid)
    # print(current_sand)
    y, x = current_sand
    if grid[y+1, x] == 0:
        grid[current_sand] = 0
        current_sand = (y+1, x)
        grid[current_sand] = - 1
    elif grid[y+1, x-1] == 0:
        grid[current_sand] = 0
        current_sand = (y+1, x-1)
        grid[current_sand] = - 1
    elif grid[y+1, x+1] == 0:
        grid[current_sand] = 0
        current_sand = (y+1, x+1)
        grid[current_sand] = - 1
    else:
        ans += 1
        grid[current_sand] = 1
        current_sand = init_sand
        grid[current_sand] = -1
    # sleep(0.07)
    # print(grid[0:20, :20])
    # print()
    

print(ans)
