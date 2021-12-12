from copy import copy
from collections import defaultdict

def is_big(s):
    return s<'a'


def get_num_paths_to(dst, link_map, visit_count, solution, chosen_small=None):
    solution = dst+','+solution
    if dst == 'start':
        #print(solution)
        return 1

    visit_count = copy(visit_count)
    visit_count[dst] += 1
    num_visits = visit_count[dst]

    if not is_big(dst):
        if chosen_small is None:
            if num_visits >= 2:
                chosen_small = dst
        else:
            #we've already picked a small cave
            max_visits = 1
            if dst == chosen_small:
                max_visits += 1
            if num_visits > max_visits:
                return 0

    num_paths = 0
    for src in link_map[dst]:
        if src != 'end':
            num_paths += get_num_paths_to(src, link_map, visit_count, solution, chosen_small)
    return num_paths


def main():
    fn = 'input.txt'
    #fn = 'test1.txt'

    with open(fn, 'r') as f:
        lines = [li.strip() for li in f.readlines()]

    link_map = defaultdict(list)
    visit_count = defaultdict(int)

    for li in lines:
        a, b = li.split('-')
        link_map[a].append(b)
        link_map[b].append(a)

    print(get_num_paths_to('end', link_map, visit_count, ''))



if __name__ == '__main__':
    main()

