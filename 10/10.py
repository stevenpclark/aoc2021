lr_map = {'{':'}', '[':']', '(':')', '<':'>'}
illegal_score_map = {')': 3, ']': 57, '}': 1197, '>': 25137}
completion_score_map = {')': 1, ']': 2, '}': 3, '>': 4}


def main():
    #fn = 'test.txt'
    fn = 'input.txt'

    with open(fn, 'r') as f:
        lines = [li.strip() for li in f]

    p1_score = 0
    p2_scores = list()
    for li in lines:
        stack = list()
        for c in li:
            if c in '[{(<':
                stack.append(c)
            else:
                assert c in ']})>'
                left = stack.pop()
                if lr_map[left] != c:
                    p1_score += illegal_score_map[c]
                    break
        else:
            completion_str = ''.join([lr_map[c] for c in reversed(stack)])
            completion_score = 0
            for c in completion_str:
                completion_score = completion_score*5 + completion_score_map[c]
            p2_scores.append(completion_score)

    print(p1_score)

    p2_scores.sort()
    print(p2_scores[len(p2_scores)//2])


if __name__ == '__main__':
    main()
