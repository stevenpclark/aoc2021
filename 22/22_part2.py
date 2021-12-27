from itertools import product
import numpy as np

CMD_MAP = {'off': False, 'on': True}

class Solid:
    def __init__(self, mode, bounds, name):
        self.mode = mode
        self.bounds = bounds
        self.ndim, _ = bounds.shape
        self.children = None
        self.name = name
        assert self.get_volume() > 0

    def get_volume(self):
        if self.children is not None:
            return sum(c.get_volume() for c in self.children)
        else:
            return np.prod(np.diff(self.bounds)+1)

    def _intersects(self, other):
        #if any dimension does not have overlap, return False
        #else, return True
        for d in range(self.ndim):
            amin, amax = self.bounds[d, :]
            bmin, bmax = other.bounds[d, :]
            if not (amin<=bmin<=amax or amin<=bmax<=amax or bmin<=amin<=bmax or bmin<=amax<=bmax):
                return False
        return True

    def subtract(self, other):
        #print(f'{self.name} is subtracting {other.name}')
        #modify self, do not modify other
        if not self._intersects(other):
            #print(f'{other.name} doesnt intersect with {self.name}')
            return
        if self.children is not None:
            #print(f'{self.name} calling subtract on {len(self.children)} children')
            for c in self.children:
                c.subtract(other)
        elif other.children is not None:
            for c in other.children:
                self.subtract(c)
        else:
            self.children = list()
            #split self into chunks
            #remove single chunk that overlaps with subtract
            #add all other chunks as children of self
            safe_bounds = list()
            shared_region = list()
            for d in range(self.ndim):
                d_list = list()
                if self.bounds[d, 0] < other.bounds[d, 0]:
                    d_list.append([self.bounds[d,0], other.bounds[d,0]-1])
                if other.bounds[d, 1] < self.bounds[d, 1]:
                    d_list.append([other.bounds[d,1]+1, self.bounds[d,1]])
                shared_range = [max(self.bounds[d,0],other.bounds[d,0]), min(self.bounds[d,1],other.bounds[d,1])]
                shared_region.append(shared_range)
                d_list.append(shared_range)
                safe_bounds.append(d_list)
            shared_region = tuple(shared_region)
            n = 0
            for bounds_group in product(*safe_bounds):
                if bounds_group != shared_region:
                    self.children.append(Solid(self.mode, np.array(bounds_group), name='%s_c%d'%(self.name,n)))
                    n += 1
            #print(f'{self.name} spawned {len(self.children)} children')


def main():
    fn = 'input.txt'

    with open(fn, 'r') as f:
        lines = [li.strip() for li in f.readlines()]

    input_solids = list()
    n = 0
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
        input_solids.append(Solid(cmd, bounds, name='solid_%d'%n))
        n += 1

    assert input_solids[0].mode

    solids = [input_solids[0]]

    for s2 in input_solids[1:]:
        #print(sum(s.get_volume() for s in solids))
        #interact s2 against all existing solids
        #find all existing solids that are relevant
        #if s2 is "off" mode, we are subtracting the entirety of s2 from other solids
        #if s2 is "on" mode, we are subtracting parts from s2 and then adding remaining parts to solids list
        if s2.mode:
            #on mode
            for s1 in solids:
                s2.subtract(s1)
            solids.append(s2)
        else:
            #off mode
            for s1 in solids:
                s1.subtract(s2)

    print(sum(s.get_volume() for s in solids))





if __name__ == '__main__':
    main()
