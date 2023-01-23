import numpy as np
from time import sleep

with open('inputs/inputx20.txt', 'r') as f:
    cycle = list(map(int, f.read().strip().split('\n')))

n = len(cycle)
order = cycle.copy()

print(cycle)
print()

shift = 0
for i, current in enumerate(order):
    i_shift = i + shift
    print('round of', current, 'i=', i, 'shifted_i=', i_shift)
    a = cycle.pop(i_shift%n)
    print(cycle)
    # assert a == current

    cycle.insert((i_shift + current)%(n-1), current)
    print(cycle)

    if (i_shift + current)%(n-1) > i:
        print(shift, '-->', end=' ')
        shift -= 1
        print(shift)
    elif (i_shift + current)%(n-1) < i:
        print(shift, '--> 0', end='\n')
        shift = 0
    


    # elif (i_shift + current)%(n-1) < i:
    #     print(shift, '-->', end=' ')
    #     shift += 1
    #     print(shift)
    
    print()

zero = cycle.index(0)
print(zero)
print(cycle[(1000+zero)%n], cycle[(2000+zero)%n], cycle[(3000+zero)%n])
ans = cycle[1000%n] + cycle[2000%n] + cycle[3000%n]
print(ans)
