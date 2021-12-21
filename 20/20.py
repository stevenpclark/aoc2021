import numpy as np
from scipy import ndimage

char_map = {'.':0, '#':1}

kern = np.array([2**n for n in range(8,-1,-1)], dtype=np.uint16).reshape(3,3)
kern = np.flip(kern)

def main():
    #fn = 'test.txt'
    fn = 'input.txt'

    with open(fn, 'r') as f:
        lines = [[char_map[c] for c in li.strip()] for li in f.readlines()]

    algo = np.array(lines[0], dtype=np.uint16)

    g_start = np.array(lines[2:])
    nr, nc = g_start.shape

    num_gens = 50
    BUF = num_gens*2
    g = np.zeros((BUF*2+nr, BUF*2+nc), dtype=np.uint16)
    g[BUF:nr+BUF, BUF:nc+BUF] = g_start
    nr, nc = g.shape

    for i in range(num_gens):
        g = algo[ndimage.convolve(g, kern, mode='constant', cval=0)]

    HB = BUF//2
    g[0:HB,:] = 0
    g[:,0:HB] = 0
    g[nr-HB:nr,:] = 0
    g[:,nc-HB:nc] = 0

    print(g.sum())


if __name__ == '__main__':
    main()
