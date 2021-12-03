import numpy as np

def filter_data(data, use_most_common):
    _, nc = data.shape
    for c in range(nc):
        nr, _ = data.shape
        if nr <= 1:
            break
        
        col_score = sum(data[:,c])/nr
        if use_most_common:
            keep_val = col_score >= 0.5
        else:
            keep_val = col_score < 0.5

        mask = data[:,c] == keep_val
        data = data[mask, :]

    x = 0
    for n in data[0,:]:
        x = (x << 1) + n

    return x


def main():
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

    rating1 = filter_data(data, use_most_common=True)
    rating2 = filter_data(data, use_most_common=False)

    print(rating1*rating2)


if __name__ == '__main__':
    main()
