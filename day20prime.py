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

MARGIN = 2
MARGINX = 200

grid = np.zeros((maxy + MARGIN + 1, maxx - minx + MARGINX*2))
grid[-1, :] = np.ones((1, maxx - minx + MARGINX*2))

print(minx, maxx, miny, maxy)

for el in elements:
    for i in range(1, len(el)):
        if el[i][0] == el[i-1][0]:  # y constant
            if el[i][1] < el[i-1][1]:
                grid[el[i][0], el[i][1] - minx + MARGINX: el[i-1][1] - minx + MARGINX +1] = [1] * abs(el[i][1] - el[i-1][1] -1)
            else:
                grid[el[i][0], el[i-1][1] - minx + MARGINX: el[i][1] - minx + MARGINX +1] = [1] * abs(el[i][1] - el[i-1][1] +1)
        elif el[i][1] == el[i-1][1]:  # x constant
            if el[i][0] < el[i-1][0]:
                # print(len(grid[el[i][0]:el[i-1][0]+1, el[i][1] - minx + MARGIN]))
                # print(len([1] * abs(el[i][0] - el[i-1][0] -1)))
                # print()
                # print(el[i][0], el[i-1][0]+1, el[i][1] - minx + MARGIN,)
                grid[el[i][0]:el[i-1][0]+1, el[i][1] - minx + MARGINX] = [1] * abs(el[i][0] - el[i-1][0] -1)
            else:
                grid[el[i-1][0]:el[i][0]+1, el[i][1] - minx + MARGINX] = [1] * abs(el[i][0] - el[i-1][0] +1)

init_sand = (0, 500 - minx + MARGINX)
grid[init_sand] = -1
m, n = grid.shape

current_sand = (0, 0)
ans = 1
first = True

while True:
    # print(grid[current_sand[0], current_sand[1]:])
    # print(grid)
    # print(current_sand)
    if first:
        current_sand = init_sand
        first = False
    y, x = current_sand

    if grid[y+1, x] == 0:
        grid[current_sand] = 0
        current_sand = (y+1, x)
        grid[current_sand] = - 1
    elif grid[y+1, x-1] == 0:
        grid[current_sand] = 0
        current_sand = (y+1, x-1)
        grid[current_sand] = - 1
    elif grid[y+1, x+1:x+2] == 0:
            grid[current_sand] = 0
            current_sand = (y+1, x+1)
            grid[current_sand] = - 1
    elif current_sand == init_sand:
        break
    else:
        ans += 1
        grid[current_sand] = 1
        current_sand = init_sand
        grid[current_sand] = -1
    # sleep(0.07)
    # print(grid)
    # print()
    

print(ans)
