with open('input', 'r') as f:
    a = f.read().strip().split()

ans = 0
for line in a:
    first, second = [list(map(lambda a: int(a), el.split('-'))) for el in line.split(',')]
    
    if (first[0] <= second[0] and first[1] >= second[1]) or (first[0] >= second[0] and first[1] <= second[1]):
        ans += 1

print(ans)
