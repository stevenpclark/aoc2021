from itertools import permutations

T, TL, TR, M, BL, BR, B = range(7)

bars_to_digit = {
        frozenset([T, TL, TR, BL, BR, B]): 0,
        frozenset([TR, BR]): 1,
        frozenset([T, M, B, TR, BL]): 2,
        frozenset([T, M, B, TR, BR]): 3,
        frozenset([TR, BR, TL, M]): 4,
        frozenset([T, M, B, TL, BR]): 5,
        frozenset([T, M, B, TL, BL, BR]): 6,
        frozenset([TR, BR, T]): 7,
        frozenset([T, TL, TR, M, BL, BR, B]): 8,
        frozenset([T, M, B, TL, TR, BR]): 9
    }

def decode_row(inputs, outputs):
    for perm in permutations('abcdefg'):
        bar_lookup = dict(zip(perm, range(7)))
        for grp in inputs:
            bars = frozenset(bar_lookup[c] for c in grp)
            if bars not in bars_to_digit:
                break
        else:
            digits = list()
            for grp in outputs:
                bars = frozenset(bar_lookup[c] for c in grp)
                digits.append(str(bars_to_digit[bars]))
            return int(''.join(digits))

def main():
    #fn = 'test.txt'
    fn = 'input.txt'

    with open(fn, 'r') as f:
        lines = f.readlines()

    inputs = [li.split(' | ')[0].split() for li in lines]
    outputs = [li.split(' | ')[1].split() for li in lines]
    
    part1 = 0
    for out_row in outputs:
        for s in out_row:
            if len(s) in [2,3,4,7]:
                part1 += 1
    print(part1)


    print(sum(decode_row(inputs[i], outputs[i]) for i in range(len(inputs))))


if __name__ == '__main__':
    main()
