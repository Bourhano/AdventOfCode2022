with open('inputs/input6.txt', 'r') as f:
    a = f.read()  # .split('\n')

b = {}
i = 0
while len(b) != 4:
    b = set(a[i:i+4])
    i += 1

print(i+4 - 1)