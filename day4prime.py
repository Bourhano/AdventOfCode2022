with open('input', 'r') as f:
    a = f.read().strip().split()

ans = 0
for line in a:
    first, second = [list(map(lambda a: int(a), el.split('-'))) for el in line.split(',')]
    
    if not (first[1] < second[0] or first[0] > second[1]):
        ans += 1

print(ans)
