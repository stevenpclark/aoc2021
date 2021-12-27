import numpy as np

cmd_dict = {'on': True, 'off': False}

#fn = 'test.txt'
fn = 'input.txt'

with open(fn, 'r') as f:
    lines = [li.strip() for li in f.readlines()]


B = 100
g = np.zeros((200,200,200), dtype=bool)

for li in lines:
    li = li.replace('=', ' ').replace('..', ' ').replace(',', ' ')
    #TODO: regexify
    cmd, _, xmin, xmax, _, ymin, ymax, _, zmin, zmax = li.split()

    v = cmd_dict[cmd]

    xmin = int(xmin)
    xmax = int(xmax)
    ymin = int(ymin)
    ymax = int(ymax)
    zmin = int(zmin)
    zmax = int(zmax)

    if -50<=xmin<=50:
        g[B+xmin:B+xmax+1, B+ymin:B+ymax+1, B+zmin:B+zmax+1] = v

print(g.sum())

