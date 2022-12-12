import numpy as np
from scipy.sparse import csr_matrix
from sknetwork.path import get_shortest_path

with open('inputs/inputx12.txt', 'r') as f:
    a = f.read().strip().split('\n')

m, n = len(a), len(a[0])
grid = np.ones((m+2, n+2)) * -2

for i, line in enumerate(a):
    for j, el in enumerate(line):
        match el:
            case 'S':
                grid[i+1, j+1] = 0
                S = i * n + j % n
            case 'E':
                grid[i+1, j+1] = ord('z') - ord('a') + 1
                E = i * n + j % n
            case _:
                grid[i+1, j+1] = ord(el) - ord('a')

p = m*n
k = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
adj = np.zeros((m*n, m*n))
for ind_from in range(p):
    i_from, j_from = ind_from // n + 1, ind_from % n + 1
    current = grid[i_from, j_from]
    patch = grid[i_from-1:i_from+2, j_from-1:j_from+2]
    for index in [(0, 1), (1, 0), (1, 2), (2, 1)]:
        if patch[index] != -2 and patch[index] - current <= 1:
            i_to, j_to = i_from + index[0] - 1, j_from + index[1] - 1
            ind_to = (i_to - 1) * n + (j_to - 1) % n
            adj[ind_from, ind_to] = 1

path = get_shortest_path(csr_matrix(adj), sources=S, targets=E)

ans = len(path) - 1
print(ans)

# graph shortest path complexity: O(VE) [Bellman-Ford, single source single destination],
#  in our case V = m*n = 2870 and E is at most 4 per vertex, hence O(4V^2)
#  for Floyd-Warshall the complexity is O(V^3)
