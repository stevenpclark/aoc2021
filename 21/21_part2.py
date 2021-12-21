from itertools import product
from collections import Counter
import numpy as np

#7 possible roll sum values, 1 universe turns into 27
dv = [1,2,3]
roll_counts = Counter(sum(tup) for tup in product(dv,dv,dv))

def is_terminal(state):
    return state[0] >= 21 or state[1] >= 21

def get_next_states(state):
    #return list of (next_state, count) tuples
    s_a, s_b, p_a, p_b, turn = state
    new_turn = (turn+1)%2

    results = list()
    for roll_sum, count in roll_counts.items():
        p_a_new = ((p_a-1+roll_sum)%10)+1
        next_state = (s_b, s_a+p_a_new, p_b, p_a_new, new_turn)
        results.append((next_state, count))

    return results

def main():
    #p_start = (4,8)
    p_start = (8,3)

    #state: s_a * s_b * p_a * p_b * turn
    start_state = (0,0,p_start[0],p_start[1],0)
    uni_counts = Counter([start_state])

    done = False
    while not done:
        prev_counts = uni_counts
        uni_counts = Counter()
        done = True
        for state, count in prev_counts.items():
            if is_terminal(state):
                uni_counts[state] += count
            else:
                done = False
                for next_state, multiplier in get_next_states(state):
                    uni_counts[next_state] += (count*multiplier)

    p1_wins, p2_wins = 0,0
    for state, count in uni_counts.items():
        if state[-1] == 0:
            p1_wins += count
        else:
            p2_wins += count
    print(max(p1_wins, p2_wins))

if __name__ == '__main__':
    main()
