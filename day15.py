import numpy as np

HEIGHT = 2000000

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
height = HEIGHT-miny
line_at_height = np.zeros(w, np.int8)

sensors_x -= minx
sensors_y -= miny
beacons_x -= minx
beacons_y -= miny

elements_at_height = set()
for i in range(n):
    distance = distances[i]

    if beacons_y[i] == height:
        elements_at_height.add((beacons_y[i], beacons_x[i]))
    if sensors_y[i] == height:
        elements_at_height.add((sensors_y[i], sensors_x[i]))

    range_x = sensors_x[i] - distance, sensors_x[i] + distance

    y = height
    for x in range(*range_x):
        manhattan = np.abs(x - sensors_x[i]) + np.abs(y - sensors_y[i])
        if manhattan <= distance:
            line_at_height[x] = -1


ans = np.sum(line_at_height == -1) - len(elements_at_height)
print(ans)
