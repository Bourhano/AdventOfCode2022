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

LENGTH = 10

snake = [Point() for _ in range(LENGTH)]
d = Point()
visited = [(0, 0)]
for line in a:
    direction, count = line.split()

    for _ in range(int(count)):
        head = snake[0]
        match direction:
            case 'D':
                head += Point(1, 0)
            case 'U':
                head += Point(-1, 0)
            case 'L':
                head += Point(0, -1)
            case 'R':
                head += Point(0, 1)
        snake[0] = head

        for i in range(LENGTH-1):
            head = snake[i]
            tail = snake[i+1]

            d = head - tail
            # print("i=", i, d.x, d.y, end=', ')
            if abs(d.x) + abs(d.y) > 1 and not (abs(d.x) == abs(d.y) and abs(d.x) == 1):
                if d.x == 0:
                    mvt = Point(d.x, d.y - 1 if d.y > 0 else d.y + 1)
                elif d.y == 0:
                    mvt = Point(d.x - 1 if d.x > 0 else d.x + 1, d.y)
                elif abs(d.x) > abs(d.y):
                    mvt = Point(d.x - 1 if d.x > 0 else d.x + 1, d.y)
                elif abs(d.x) < abs(d.y):
                    mvt = Point(d.x, d.y - 1 if d.y > 0 else d.y + 1)
                else:
                    mvt = Point(d.x - 1 if d.x > 0 else d.x + 1, d.y - 1 if d.y > 0 else d.y + 1)
                tail += mvt
                # print(mvt.x, mvt.y)

        if i == (LENGTH - 1) - 1:
            visited.append(tail.get_pt())

        snake[i] = head
        snake[i+1] = tail

ans = len(set(visited))
print(ans)
