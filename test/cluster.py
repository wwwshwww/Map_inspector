import cv2
import numpy as np
import math
import collections
import matplotlib.pyplot as plt

def main():
    im = np.zeros([500, 500], dtype=int);
    im[2,2] = 255
    im[4,35] = 255
    im[42,7] = 255
    im[48, 40] = 255
    im[25,1] = 255
    im[22,26] = 255
    im[23,25] = 255

    im[455,455] = 255
    im[451,456] = 255

    points = np.where(im>=255)
    used = np.full_like(im, False)
    size = 50
    clusters = collections.deque()

    ereas = 0
    ereae = len(im)-1

    for (i, j) in zip(points[0], points[1]):
        print(used[i,j], (i,j))
        if used[i,j]: continue
        print(f"\n===={i,j}====\n")
        tmp = collections.deque()
        clust = collections.deque()
        tmp.append((i, j))
        clust.append((i, j))
        used[i,j] = True
        while not len(tmp)==0:
            print(tmp)
            pt = tmp.pop()
            si = max(ereas, pt[0]-size)
            ei = min(ereae, pt[0]+size)
            sj = max(ereas, pt[1]-size)
            ej = min(ereae, pt[1]+size)
            f = np.where(im[si:ei+1, sj:ej+1]>=255)
            print((i,j),f)
            grid_i, grid_j = np.meshgrid(range(si,ei+1), range(sj,ej+1), indexing='ij')
            print(grid_i, grid_j)
            for (ii, jj) in zip(f[0], f[1]):
                tmp_p = (grid_i[ii,jj], grid_j[jj,jj])
                print(tmp_p)
                if used[tmp_p]: continue
                used[tmp_p] = True
                print(tmp_p,"2")
                tmp.append(tmp_p)
                clust.append(tmp_p)
        clusters.append(clust)
    
    print(clusters)
    

if __name__ == "__main__":
    main()