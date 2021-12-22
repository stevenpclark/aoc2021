import numpy as np

CMD_MAP = {'off': False, 'on': True}

class Solid:
    def __init__(self, mode, bounds):
        self.mode = mode
        self.bounds = bounds
        self.ndim, _ = bounds.shape
        assert self.get_volume() > 0

    def get_volume(self):
        return np.prod(np.diff(self.bounds)+1)

    def intersects(self, other):
        #if any dimension does not have overlap, return False
        #else, return True
        for d in range(self.ndim):
            amin, amax = self.bounds[d, :]
            bmin, bmax = other.bounds[d, :]
            if not (amin<=bmin<=amax or amin<=bmax<=amax or bmin<=amin<=bmax or bmin<=amax<=bmax):
                return False
        return True


def main():
    fn = 'test.txt'

    with open(fn, 'r') as f:
        lines = [li.strip() for li in f.readlines()]

    input_solids = list()
    for li in lines:
        li = li.replace('=', ' ').replace(',', ' ').replace('..', ' ')
        cmd, _, xmin, xmax, _, ymin, ymax, _, zmin, zmax = li.split()
        cmd = CMD_MAP[cmd]
        xmin = int(xmin)
        ymin = int(ymin)
        zmin = int(zmin)
        xmax = int(xmax)
        ymax = int(ymax)
        zmax = int(zmax)
        bounds = np.array([[xmin, xmax], [ymin, ymax], [zmin, zmax]])
        input_solids.append(Solid(cmd, bounds))

    assert input_solids[0].mode

    solids = [input_solids[0]]

    for s2 in input_solids[1:]:
        #interact s2 against all existing solids
        #find all existing solids that are relevant
        #if s2 is "off" mode, we are subtracting parts from other solids
        #if s2 is "on" mode, we are subtracting parts from s2 and then adding remaining parts to solids list
        relevant_solids = [s1 for s1 in solids if s1.intersects(s2)]

        if s2.mode:
            #on mode






if __name__ == '__main__':
    main()
