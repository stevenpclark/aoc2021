test = (4,8)
my_input = (8,3)




def main():
    positions = list(my_input)
    last_roll = 0
    num_rolls = 0
    scores = [0,0]

    while scores[0] < 1000 and scores[1] < 1000:
        for turn in range(2):
            total_roll = 0
            for i in range(3):
                roll = (last_roll%100)+1
                total_roll += roll
                last_roll = roll
                num_rolls += 1
            p = positions[turn]
            p = ((p-1 + total_roll)%10)+1
            positions[turn] = p
            scores[turn] += p
            if scores[0] >= 1000 or scores[1] >= 1000:
                break

    print(min(scores)*num_rolls)


    

if __name__ == '__main__':
    main()
