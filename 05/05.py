import numpy as np

g = np.zeros((2000,2000), dtype=np.int)

fn = 'input.txt'
#fn = 'test.txt'

with open(fn, 'r') as f:
    lines = f.readlines()

for li in lines:
    src, dst = li.split(' -> ')

    v1 = [int(s) for s in src.split(',')]
    v2 = [int(s) for s in dst.split(',')]

    v1, v2 = sorted([v1, v2])

    c1, r1 = v1
    c2, r2 = v2

    if r1==r2 or c1==c2:
        #print(c1, r1, c2, r2)
        g[r1:r2+1, c1:c2+1] += 1
        #print(g)
    else:
        if r2 > r1:
            dr = 1
        else:
            dr = -1
        r = r1
        for i, c in enumerate(range(c1, c2+1)):
            g[r, c] += 1
            r += dr

print(g)
print((g>=2).sum())


