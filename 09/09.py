import numpy as np
from scipy.signal import argrelextrema, argrelmin #thanks stackoverflow!

fn = 'test.txt'

with open(fn, 'r') as f:
    lines = [list(map(int, list(li.strip()))) for li in f.readlines()]

g = np.array(lines)
print(g)

print(argrelmin(g))
