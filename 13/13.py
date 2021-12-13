import numpy as np

def main():
    fn = 'input.txt'

    with open(fn, 'r') as f:
        lines = [li.strip() for li in f.readlines()]

    done_points = False

    points = set()
    folds = list()
    for li in lines:
        if not li:
            done_points = True
            continue
        if done_points:
            li = li.split('=')
            li = (li[0][-1], int(li[1]))
            folds.append(li)
        else:
            pt = tuple(int(s) for s in li.split(','))
            points.add(pt)

    print(folds)
    print(points)

    for axis, fold_val in folds:
        for pt in list(points):
            if axis == 'x':
                if pt[0] > fold_val:
                    new_pt = (2*fold_val-pt[0], pt[1])
                    points.remove(pt)
                    points.add(new_pt)
            else:
                if pt[1] > fold_val:
                    new_pt = (pt[0], 2*fold_val-pt[1])
                    points.remove(pt)
                    points.add(new_pt)

    print(len(points))


    max_x = max([pt[0] for pt in points])
    max_y = max([pt[1] for pt in points])

    g = np.zeros((max_y+1, max_x+1), dtype=np.uint8)
    np.set_printoptions(linewidth=np.inf)
    for pt in points:
        g[pt[1],pt[0]] = 1
    print(g)
    
                
            
        


if __name__ == '__main__':
    main()
