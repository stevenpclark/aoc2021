def main():
    fn = 'input.txt'
    #fn = 'test.txt'
    with open(fn, 'r') as f:
        lines = f.readlines()

    x, y = 0, 0
    for li in lines:
        cmd, n = li.split()
        n = int(n)

        if cmd == 'forward':
            x += n
        elif cmd == 'down':
            y += n
        elif cmd == 'up':
            y -= n
        else:
            raise ValueError
    print(x*y)

    x, y, aim = 0, 0, 0
    for li in lines:
        cmd, n = li.split()
        n = int(n)

        if cmd == 'forward':
            x += n
            y += aim*n
        elif cmd == 'down':
            aim += n
        elif cmd == 'up':
            aim -= n
        else:
            raise ValueError
    print(x*y)

if __name__ == '__main__':
    main()
