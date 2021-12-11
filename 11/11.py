import numpy as np
from scipy import ndimage

def main():
    #fn = 'simple.txt'
    #fn = 'test.txt'
    fn = 'input.txt'

    with open(fn, 'r') as f:
        lines = [list(li.strip()) for li in f.readlines()]

    g = np.array(lines, dtype=np.uint8)
    nr, nc = g.shape

    kern = np.ones((3,3), dtype=np.uint8)
    kern[1,1] = 0

    num_flashes = 0
    for i in range(1, 1000):
        g += 1
        flash_map = np.zeros((nr, nc), dtype=np.uint8)
        new_flashes = (g==10).astype(np.uint8)
        while new_flashes.any():
            num_flashes += new_flashes.sum()
            flash_map = flash_map | new_flashes
            sum_map = ndimage.convolve(new_flashes, kern, mode='constant', cval=0)
            g += sum_map
            new_flashes = (g>9).astype(np.uint8) & (np.logical_not(flash_map))
        g[g>=10] = 0
        if i == 100:
            print(int(num_flashes))
        if flash_map.all():
            print(i)
            break


if __name__ == '__main__':
    main()
