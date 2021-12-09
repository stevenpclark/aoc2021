import numpy as np

#fn = 'test.txt'
fn = 'input.txt'

with open(fn, 'r') as f:
    s = f.read()

xs = np.array([int(c) for c in s.split(',')])

x1 = xs.min()
x2 = xs.max()

best = 1e9
for i in range(x1, x2+1):
    val = abs(xs-i).sum()
    if val < best:
        best = val
    else:
        print(best)
        break

best = 1e9
for i in range(x1, x2+1):
    inner = abs(xs-i)
    val = ((inner*(inner+1))/2).sum()
    if val < best:
        best = val
    else:
        print(int(best))
        break
