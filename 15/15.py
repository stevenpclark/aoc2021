import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path

def part_twoify(g):
    nr, nc = g.shape
    g2 = np.tile(g, (5,5))
    return g2

def main():
    #fn = 'tiny.txt'
    #fn = 'test.txt'
    fn = 'input.txt'

    with open(fn, 'r') as f:
        lines = [li.strip() for li in f.readlines()]

    lines = [[int(c) for c in li] for li in lines]

    g = np.array(lines)

    #g = part_twoify(g)
    print(g)

    nr, nc = g.shape
    print(nr, nc)
    count = nr*nc

    t_costs = np.zeros((count, count))

    def rc_to_i(r,c):
        return r*nc + c

    for r in range(nr):
        for c in range(nc):
            i1 = rc_to_i(r,c)
            neighbors = list()
            if r>=1:
                neighbors.append((r-1,c))
            if c>=1:
                neighbors.append((r,c-1))
            if r<nr-1:
                neighbors.append((r+1,c))
            if c<nc-1:
                neighbors.append((r,c+1))
            for r2,c2 in neighbors:
                i2 = rc_to_i(r2,c2)
                t_costs[i1,i2] = g[r2,c2]
                t_costs[i2,i1] = g[r,c]

    graph = csr_matrix(t_costs)
    #print(graph)

    dist_matrix = shortest_path(csgraph=graph, directed=True, indices=0, return_predecessors=False, method='auto')
    print(int(dist_matrix[-1]))







if __name__ == '__main__':
    main()
