import numpy as np
from numpy.lib.stride_tricks import sliding_window_view


def get_num_increasing(li, window_shape):
    return np.sum(np.diff(np.sum(sliding_window_view(li, window_shape), axis=1))>0)

def main():
    fn = 'input.txt'
    #fn = 'test.txt'
    with open(fn, 'r') as f:
        li = [int(s) for s in f.readlines()]

    print(get_num_increasing(li, 1))
    print(get_num_increasing(li, 3))


if __name__ == '__main__':
    main()
