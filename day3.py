with open('input', 'r') as f:
    a = f.read().strip().split()

ans = 0
for line in a:
    ln = len(line)//2
    in1 = set(line[:ln])
    in2 = set(line[ln:])
    out = in1 - in2
    inter = (in1 - out).pop()
    
    if inter.islower():
        ans += ord(inter) - ord('a') + 1
    else:
        ans += ord(inter) - ord('A') + 27

print(ans)
