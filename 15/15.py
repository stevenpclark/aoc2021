from math import inf
from collections import defaultdict
import heapq
import numpy as np

def part_twoify(world):
    nr, nc = world.shape
    world2 = np.tile(world, (5,5))
    for tr in range(5):
        for tc in range(5):
            inc = tr+tc
            world2[tr*nr:(tr+1)*nr, tc*nc:(tc+1)*nc] += inc
    world2[world2>9] -= 9
    return world2

def h(n, goal):
    #must not over-estimate
    r1, c1 = n
    r2, c2 = goal
    return abs(r2-r1)+abs(c2-c1)


def a_star(world):
    #https://en.wikipedia.org/wiki/A*_search_algorithm
    nr, nc = world.shape
    start = (0, 0)
    goal = (nr-1, nc-1)

    def get_neighbors(n):
        r, c = n
        neighbors = list()
        if r >= 1:
            neighbors.append((r-1, c))
        if c >= 1:
            neighbors.append((r, c-1))
        if r < nr-1:
            neighbors.append((r+1, c))
        if c < nc-1:
            neighbors.append((r, c+1))
        return neighbors

    g_score = defaultdict(lambda:inf)
    g_score[start] = 0

    f_score = defaultdict(lambda:inf)
    f_score[start] = h(start, goal)

    open_heap = []
    in_heap_set = set()
    heapq.heappush(open_heap, (f_score[start], start))
    in_heap_set.add(start)

    while open_heap:
        _, current = heapq.heappop(open_heap)
        in_heap_set.remove(current)
        if current == goal:
            print(g_score[goal])
            return

        for n2 in get_neighbors(current):
            tentative_g_score = g_score[current] + world[n2]
            if tentative_g_score < g_score[n2]:
                g_score[n2] = tentative_g_score
                f_score[n2] = tentative_g_score + h(n2, goal)
                if n2 not in in_heap_set:
                    heapq.heappush(open_heap, (f_score[n2], n2))
                    in_heap_set.add(n2)

    print('failure')


def main():
    #fn = 'tiny.txt'
    #fn = 'test.txt'
    fn = 'input.txt'

    with open(fn, 'r') as f:
        lines = [li.strip() for li in f.readlines()]

    lines = [[int(c) for c in li] for li in lines]

    world = np.array(lines)

    world = part_twoify(world)

    a_star(world)


if __name__ == '__main__':
    main()
