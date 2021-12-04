import numpy as np

def get_board_score(board, call):
    return call*board[board>0].sum()


def main():
    fn = 'input.txt'
    #fn = 'test.txt'

    with open(fn, 'r') as f:
        lines = f.readlines()

    calls = [int(s) for s in lines[0].split(',')]

    boards = list()

    for i in range(2, len(lines), 6):
        b = np.fromstring(''.join(lines[i:i+5]), dtype=int, sep=' ').reshape(5,5)
        boards.append(b)

    boards = np.array(boards)

    num_boards, _, _ = boards.shape

    done_part1 = False
    num_wins = 0
    ignore_board = [False]*num_boards
    for call in calls:
        boards[boards==call] = -1

        for i, board in enumerate(boards):
            if ignore_board[i]:
                continue
            if -5 in board.sum(axis=0) or -5 in board.sum(axis=1):
                if not done_part1:
                    print(get_board_score(board, call))
                    done_part1 = True
                num_wins += 1
                ignore_board[i] = True
                if num_wins == num_boards:
                    print(get_board_score(board, call))
                    return

if __name__ == '__main__':
    main()
