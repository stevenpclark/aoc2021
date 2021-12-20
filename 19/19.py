from itertools import combinations
from scipy.spatial.transform import Rotation as R
import numpy as np

#surely there's a better way to make the 24 rots than this...
ROTS = [
    R.from_euler('z',   0, degrees=True),
    R.from_euler('z',  90, degrees=True),
    R.from_euler('z', 180, degrees=True),
    R.from_euler('z', 270, degrees=True),
    R.from_euler('xz', [ 90,   0], degrees=True),
    R.from_euler('xz', [ 90,  90], degrees=True),
    R.from_euler('xz', [ 90, 180], degrees=True),
    R.from_euler('xz', [ 90, 270], degrees=True),
    R.from_euler('xz', [180,   0], degrees=True),
    R.from_euler('xz', [180,  90], degrees=True),
    R.from_euler('xz', [180, 180], degrees=True),
    R.from_euler('xz', [180, 270], degrees=True),
    R.from_euler('xz', [270,   0], degrees=True),
    R.from_euler('xz', [270,  90], degrees=True),
    R.from_euler('xz', [270, 180], degrees=True),
    R.from_euler('xz', [270, 270], degrees=True),

    R.from_euler('yz', [ 90,   0], degrees=True),
    R.from_euler('yz', [ 90,  90], degrees=True),
    R.from_euler('yz', [ 90, 180], degrees=True),
    R.from_euler('yz', [ 90, 270], degrees=True),
    R.from_euler('yz', [270,   0], degrees=True),
    R.from_euler('yz', [270,  90], degrees=True),
    R.from_euler('yz', [270, 180], degrees=True),
    R.from_euler('yz', [270, 270], degrees=True),
]

ROTS = [r.as_matrix().astype(np.int8) for r in ROTS]
N_ROTS = len(ROTS) #24


class Scanner:
    def __init__(self, lines):
        self.scanner_id = int(lines[0].replace('--- scanner ','').replace(' ---',''))
        self.is_fixed = False
        self.pos = np.array([0, 0, 0])
        input_pts = np.array([eval(li) for li in lines[1:]])
        self.pts = np.zeros((N_ROTS, len(input_pts), 3), dtype=np.int32)
        self.delta_set_list = [set() for i in range(N_ROTS)]
        for i, rot in enumerate(ROTS):
            for j, pt in enumerate(input_pts):
                self.pts[i, j, :] = rot@pt
            for a, b in combinations(self.pts[i, :, :], 2):
                self.delta_set_list[i].add(tuple(a-b))
                self.delta_set_list[i].add(tuple(b-a))

    def fix(self, rot_ind):
        self.pts = self.pts[rot_ind]
        self.delta_set = self.delta_set_list[rot_ind]
        self.is_fixed = True
        self.pt_lookup = dict()
        for a, b in combinations(self.pts[:, :], 2):
            self.pt_lookup[tuple(a-b)] = a
            self.pt_lookup[tuple(b-a)] = b


    def match_and_fix(self, other):
        assert other.is_fixed
        scores = list()
        for i in range(N_ROTS):
            num_intersections = len(other.delta_set.intersection(self.delta_set_list[i]))
            scores.append((num_intersections, i))
        scores.sort()
        best_score, best_ind = scores[-1]
        if best_score >= 66: #TODO dbl-check correct threshold. 12*11/2?
            self.fix(best_ind)
            self._shift_relative_to(other)
            return True
        else:
            return False

    def _shift_relative_to(self, other):
        shared_deltas = other.delta_set.intersection(self.delta_set)
        #print(self.scanner_id)
        #for dtup in shared_deltas:
            #p2 = self.pt_lookup[dtup]
            #p1 = other.pt_lookup[dtup]
            #print(p2-p1)
        dtup = shared_deltas.pop() #TODO risky to only check 1?
        p2 = self.pt_lookup[dtup]
        p1 = other.pt_lookup[dtup]
        shift = p2-p1
        self.pts[:,:] -= shift
        self.pos = -shift
        #print(self.scanner_id, self.pos)
        #TODO: is this required?
        #self.pt_lookup = dict()
        #for a, b in combinations(self.pts[:, :], 2):
            #self.pt_lookup[tuple(a-b)] = a
            #self.pt_lookup[tuple(b-a)] = b


    def __repr__(self):
        return f'scanner {self.scanner_id}'


def main():
    #fn = 'test.txt'
    fn = 'input.txt'

    with open(fn, 'r') as f:
        lines = [li.strip() for li in f.readlines()]

    scanners = list()
    chunk = list()
    for li in lines:
        if li:
            chunk.append(li)
        else:
            scanners.append(Scanner(chunk))
            chunk = list()
    if chunk:
        scanners.append(Scanner(chunk))

    scanners[0].fix(0)
    fixed = [scanners[0]]
    not_fixed = scanners[1:]

    while not_fixed:
        for nf in not_fixed[:]:
            for f in fixed[:]:
                if nf.match_and_fix(f):
                    not_fixed.remove(nf)
                    fixed.append(nf)
                    break

    all_pts = set()
    for scanner in scanners:
        for pt in scanner.pts:
            all_pts.add(tuple(pt))
    print(len(all_pts))

    distances = list()
    for s1, s2 in combinations(scanners, 2):
        d = (np.abs(s1.pos-s2.pos)).sum()
        distances.append(d)

    distances.sort()
    print(distances[-1])

if __name__ == '__main__':
    main()
