import numpy as np
from tqdm import tqdm


MAX = 4000000

with open('inputs/inputx15.txt', 'r') as f:
    a = f.read().strip().split('\n')

n = len(a)
sensors_x, sensors_y, beacons_x, beacons_y = np.zeros(n, int), np.zeros(n, int), np.zeros(n, int), np.zeros(n, int)
for i, line in enumerate(a):
    sensor, beacon = line.split('at ')[1:3]

    sensor = sensor.split(':')[0].split('=')
    sensor_x, sensor_y = int(sensor[1].split(',')[0]), int(sensor[2])

    beacon = beacon.split('=')
    beacon_x, beacon_y = int(beacon[1].split(',')[0]), int(beacon[2])

    sensors_x[i] = sensor_x
    sensors_y[i] = sensor_y

    beacons_x[i] = beacon_x
    beacons_y[i] = beacon_y

distances_x = np.abs(sensors_x-beacons_x)
distances_y = np.abs(sensors_y-beacons_y)
distances = np.add(distances_x, distances_y)

maxx = np.max(sensors_x+distances)
maxy = np.max(sensors_y+distances)
minx = np.min(sensors_x-distances)
miny = np.min(sensors_y-distances)

h, w = maxy - miny, maxx - minx

sensors_x -= minx
sensors_y -= miny
beacons_x -= minx
beacons_y -= miny

elements_at_height = set()
bx, by = 0, 0
for y in tqdm(range(-miny, MAX-miny + 1)):
    current_line = np.ones((MAX), np.int8)
    for i in range(n):
        distance = distances[i]
        range_x = sensors_x[i] - distance, sensors_x[i] + distance

        for x in range(*range_x):
            if x < MAX-minx and y < MAX-miny and x >= -minx and y >= -miny:
                manhattan = np.abs(x - sensors_x[i]) + np.abs(y - sensors_y[i])
                if manhattan <= distance:
                    current_line[x+minx] = 0

    # print(np.mean(current_line))
    if np.sum(current_line) > 0:
        bx = np.argmax(current_line)
        by = y + miny
        break

print(bx, by)
ans = bx*MAX + by
print(ans)

# 7285459267035 too low
# 12353598000000 too high
