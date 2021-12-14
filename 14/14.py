from collections import Counter

def main():
    fn = 'input.txt'
    #fn = 'test.txt'

    with open(fn, 'r') as f:
        lines = [li.strip() for li in f.readlines()]

    p = lines[0]
    
    print(set(p))

    rules = dict()
    for li in lines[2:]:
        a, b = li.split(' -> ')
        rules[tuple(a)] = b


    for n in range(20):
        new_p = list()
        for i, c1 in enumerate(p[:-1]):
            c2 = p[i+1]
            new_c = rules[(c1, c2)]
            new_p.extend([c1, new_c])
        new_p.append(p[-1])
        p = ''.join(new_p)
        counts = Counter(p).most_common()
        #print(counts[0][1] - counts[-1][1])
        print(counts)


    
    #ss = set()
    #for i, c1 in enumerate(p[:-3]):
        #ss.add(p[i:i+4])
    #print(len(ss))
    


if __name__ == '__main__':
    main()
