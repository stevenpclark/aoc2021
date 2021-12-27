import numpy as np

CHAR_MAP = {'.':0, '>':1, 'v':2}

def main():
    #fn = 'test.txt'
    fn = 'input.txt'

    with open(fn, 'r') as f:
        lines = [[CHAR_MAP[c] for c in li.strip()] for li in f.readlines()]

    g0 = np.array(lines)
    nr, nc = g0.shape

    step = 0
    while True:
        g1 = np.zeros((nr, nc))
        for (r,c),v in np.ndenumerate(g0):
            p2 = (r, (c+1)%nc)
            if v == 1:
                if g0[p2] == 0:
                    g1[p2] = v
                else:
                    g1[r,c] = v
            elif v == 2:
                g1[r,c] = v

        g2 = np.zeros((nr, nc))
        for (r,c),v in np.ndenumerate(g1):
            p2 = ((r+1)%nr, c)
            if v == 2:
                if g1[p2] == 0:
                    g2[p2] = v
                else:
                    g2[r,c] = v
            elif v == 1:
                g2[r,c] = v

        step += 1

        if (g0 == g2).all():
            break
        g0 = g2

    print(step)

if __name__ == '__main__':
    main()
