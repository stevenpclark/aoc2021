import numpy as np
from scipy.signal import argrelextrema, argrelmin #thanks stackoverflow!

#fn = 'test.txt'
fn = 'input.txt'

with open(fn, 'r') as f:
    lines = [list(map(int, list(li.strip()))) for li in f.readlines()]

g = np.array(lines)
nr,nc = g.shape
dtype = g.dtype

#frame with nines
g2 = np.ones((nr+2,nc+2), dtype=dtype)*9
g2[1:nr+1,1:nc+1] = g
g = g2

vs = set(zip(*argrelmin(g, mode='clip', axis=0)))
hs = set(zip(*argrelmin(g, mode='clip', axis=1)))
lows = set.intersection(vs, hs)

risk = 0
for r,c in lows:
    risk += (1+g[r,c])

print(risk)

def flood(g, r, c, visited):
    if g[r,c] == 9 or (r,c) in visited:
        return 0
    visited.add((r,c))
    return 1 + (flood(g,r+1,c,visited) + flood(g,r-1,c,visited) +
                flood(g,r,c+1,visited) + flood(g,r,c-1,visited))

basin_sizes = list()
for r,c in lows:
    visited = set()
    basin_sizes.append(flood(g,r,c,visited))

basin_sizes.sort()
print(np.prod(basin_sizes[-3:]))
