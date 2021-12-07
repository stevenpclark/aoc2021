def solve(c, num_gens, memo):
    answer = memo.get((c, num_gens), None)
    if not answer:
        if num_gens <= 0:
            answer = 1
        elif c == 0:
            answer = solve(6, num_gens-1, memo) + solve(8, num_gens-1, memo)
        else:
            answer = solve(c-1, num_gens-1, memo)
    memo[(c, num_gens)] = answer
    return answer

def main():
    fn = 'input.txt'
    #fn = 'test.txt'

    with open(fn, 'r') as f:
        s = f.read()

    timers = [int(x) for x in s.split(',')]

    num_gens = 256

    memo = dict()
    
    print(sum([solve(c, num_gens, memo) for c in timers]))

if __name__ == '__main__':
    main()
