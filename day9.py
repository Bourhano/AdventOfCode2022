# type: ignore
class Point:
    "A geometirc point"
    x = 0
    y = 0

    def __init__(self, ix=0, iy=0):
        self.x = ix
        self.y = iy

    def get_pt(self):
        return (self.x, self.y)

    def __sub__(self, pt2):
        res = Point()
        res.x = self.x - pt2.x
        res.y = self.y - pt2.y
        return res

    def __add__(self, d):
        self.x += d.x
        self.y += d.y

        return self
    
with open('inputs/input9.txt', 'r') as f:
    a = f.read().strip().split('\n')

head = Point()
tail = Point()
d = Point()

visited = [(0, 0)]
for line in a:
    direction, count = line.split()

    for _ in range(int(count)):
        match direction:
            case 'D':
                head += Point(1, 0)
            case 'U':
                head += Point(-1, 0)
            case 'L':
                head += Point(0, -1)
            case 'R':
                head += Point(0, 1)

        d = head - tail
        if abs(d.x) + abs(d.y) > 1 and abs(d.x) != abs(d.y) :
            if d.x == 0:
                tail += Point(d.x, d.y - 1 if d.y > 0 else d.y + 1)
            elif d.y == 0:
                tail += Point(d.x - 1 if d.x > 0 else d.x + 1, d.y)
            elif abs(d.x) > abs(d.y):
                tail += Point(d.x - 1 if d.x > 0 else d.x + 1, d.y)
            elif abs(d.x) < abs(d.y):
                tail += Point(d.x, d.y - 1 if d.y > 0 else d.y + 1)
            
        visited.append(tail.get_pt())

ans = len(set(visited))
print(ans)
