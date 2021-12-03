import numpy as np

fn = 'input.txt'
#fn = 'test.txt'

lines = np.loadtxt(fn, dtype=str)
num_lines = len(lines)

data = np.array([[int(c) for c in s] for s in lines])

gamma_list = (np.sum(data, axis=0)/num_lines > 0.5).astype(int)
gamma = 0
epsilon = 0
for n in gamma_list:
    gamma = (gamma << 1) + n
    epsilon = (epsilon << 1) + (1-n)

print(gamma*epsilon)


j
