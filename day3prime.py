with open('input', 'r') as f:
    a = f.read().split()

ans = 0
for i in range(0, len(a), 3):
    sets = [set(el) for el in a[i:i+3]]
    inter = set.intersection(*sets).pop()

    # inter = set.intersection(*map(set,a[i:i+3])).pop()  # one liner

    if inter.islower():
        ans += ord(inter) - ord('a') + 1
    else:
        ans += ord(inter) - ord('A') + 27

print(ans)
