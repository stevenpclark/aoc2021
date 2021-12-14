from collections import Counter

def main():
    fn = 'input.txt'
    #fn = 'test.txt'

    with open(fn, 'r') as f:
        lines = [li.strip() for li in f.readlines()]

    p = lines[0]
    pair_counter = Counter([p[i:i+2] for i in range(len(p)-1)])

    lr_map = dict()
    for li in lines[2:]:
        pair, middle = li.split(' -> ')
        left = pair[0]+middle
        right = middle+pair[1]
        lr_map[pair] = [left, right]

    for n in range(40):
        old_counter = pair_counter
        pair_counter = Counter()
        for pair, count in old_counter.items():
            left, right = lr_map[pair]
            pair_counter[left] += count
            pair_counter[right] += count

    char_counter = Counter()
    for pair, count in pair_counter.items():
        char_counter[pair[0]] += count

    char_counter[p[-1]] += 1
    counts = char_counter.most_common()
    print(counts[0][1] - counts[-1][1])

if __name__ == '__main__':
    main()
