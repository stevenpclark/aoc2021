import numpy as np

def gt(a):
    return a[0]>a[1]

def lt(a):
    return a[0]<a[1]

def eq(a):
    return a[0]==a[1]

func_map = {0:np.sum, 1:np.prod, 2:np.min, 3:np.max, 5:gt, 6:lt, 7:eq}

def h2b(s):
    return bin(int(s, 16))[2:].zfill(4*len(s))

def chomp(b):
    i = 0
    version = int(b[i:i+3],2)
    i += 3
    p_type = int(b[i:i+3],2)
    i += 3
    #header now complete

    version_sum = version

    if p_type == 4:
        #literal type
        chunk = ''
        done = False
        while not done:
            chunk += b[i+1:i+5]
            if b[i] == '0':
                done = True
            i += 5
        val = int(chunk,2)
    else:
        #operator type
        length_type = int(b[i],2)
        i += 1
        target_i = 1e9
        num_sub_packets = 1e9
        if length_type == 0:
            total_length = int(b[i:i+15],2)
            i += 15
            target_i = i + total_length
        else:
            num_sub_packets = int(b[i:i+11],2)
            i += 11

        sub_packet_count = 0
        done = False
        sub_vals = list()
        while (i < target_i) and (sub_packet_count < num_sub_packets):
            i_delta, version_sum_delta, sub_val = chomp(b[i:])
            i += i_delta
            version_sum += version_sum_delta
            sub_vals.append(sub_val)
            sub_packet_count += 1

        func = func_map[p_type]

        val = int(func(sub_vals))

    return i, version_sum, val


def main():
    h = open('input.txt', 'r').read().strip()

    b = h2b(h)

    _, part1, part2 = chomp(b)

    print(part1)
    print(part2)

if __name__ == '__main__':
    main()
