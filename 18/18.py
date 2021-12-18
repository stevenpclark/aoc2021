from math import floor, ceil
from itertools import combinations

class Node:
    #TODO: could probably clean up the code by switching away from explicit
    #left / right stuff to more generic child list
    def __init__(self, li, parent=None, depth=1):
        self.left, self.right = li
        self.parent = parent
        self.depth = depth
        if isinstance(self.left, list):
            self.left = Node(self.left, self, depth+1)
        if isinstance(self.right, list):
            self.right = Node(self.right, self, depth+1)

    def magnitude(self):
        lmag = self.left
        rmag = self.right
        if isinstance(self.left, Node):
            lmag = self.left.magnitude()
        if isinstance(self.right, Node):
            rmag = self.right.magnitude()
        return 3*lmag + 2*rmag


    def move_deeper(self):
        self.depth += 1
        if isinstance(self.left, Node):
            self.left.move_deeper()
        if isinstance(self.right, Node):
            self.right.move_deeper()

    def to_list(self):
        if isinstance(self.left, Node):
            left = self.left.to_list()
        else:
            left = self.left
        if isinstance(self.right, Node):
            right = self.right.to_list()
        else:
            right = self.right
        return [left, right]

    def zeroize_child(self, child):
        if child is self.left:
            self.left = 0
        else:
            self.right = 0

    def contribute_left(self, v):
        #ascend while we are left branch
        n = self
        while (n.parent is not None) and (n is n.parent.left):
            n = n.parent
        if n.parent is None:
            return
        #n is the right child of self.parent
        #switch to the left side instead, then go right
        if isinstance(n.parent.left, int):
            n.parent.left += v
        else:
            n = n.parent.left
            while not isinstance(n.right, int):
                n = n.right
            n.right += v

    def contribute_right(self, v):
        #ascend while we are right branch
        n = self
        while (n.parent is not None) and (n is n.parent.right):
            n = n.parent
        if n.parent is None:
            return
        #n is the left child of self.parent
        #switch to the right side instead, then go left
        if isinstance(n.parent.right, int):
            n.parent.right += v
        else:
            n = n.parent.right
            while not isinstance(n.left, int):
                n = n.left
            n.left += v


    def explode(self):
        #return True if something exploded
        if isinstance(self.left, Node):
            if self.left.explode():
                return True
        if isinstance(self.right, Node):
            if self.right.explode():
                return True

        if self.depth > 4:
            self.contribute_left(self.left)
            self.contribute_right(self.right)
            self.parent.zeroize_child(self)
            return True
        return False


    def split(self):
        if isinstance(self.left, Node):
            if self.left.split():
                return True
        else:
            v = self.left
            if v >= 10:
                self.left = Node([int(floor(v/2)), int(ceil(v/2))], self, self.depth+1)
                return True

        if isinstance(self.right, Node):
            if self.right.split():
                return True
        else:
            v = self.right
            if v >= 10:
                self.right = Node([int(floor(v/2)), int(ceil(v/2))], self, self.depth+1)
                return True

        return False


def add(a, b):
    root = Node([a,b], depth=0)
    a.parent = root
    b.parent = root
    root.move_deeper()

    while True:
        if root.explode():
            continue
        if root.split():
            continue
        break

    return root


def main():
    fn = 'input.txt'

    with open(fn, 'r') as f:
        lines = [li.strip() for li in f.readlines()]

    nodes = [Node(eval(li)) for li in lines]

    n = nodes[0]
    for n2 in nodes[1:]:
        n = add(n, n2)

    print(n.magnitude())

    mags = list()
    for li1, li2 in combinations(lines, 2):
        #wasteful to re-eval each time, but oh well
        n1 = Node(eval(li1))
        n2 = Node(eval(li2))
        mags.append(add(n1,n2).magnitude())

    print(sorted(mags)[-1])

if __name__ == '__main__':
    main()

