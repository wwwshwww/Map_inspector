import cv2
import numpy as np
import math
import collections
import matplotlib.pyplot as plt

import os
import sys

this_path = os.path.dirname(__file__)

def get_test_img():
    im = np.zeros([500, 500], dtype=int)
    im[2,2] = 255
    im[4,35] = 255
    im[42,7] = 255
    im[48, 40] = 255
    im[25,1] = 255
    im[22,26] = 255
    im[23,25] = 255
    im[24,24] = 255
    im[29,29] = 255

    im[455,455] = 255
    im[451,456] = 255
    return im

class point_cluster():
    def __init__(self, img):
        self.img = img

    def get_clusters_black(self, size, erea_start=0, erea_end=None):
        if erea_end is None: 
            erea_end = len(self.img)-1
        # points = np.where(im>=255)
        points = np.where(self.img<50)
        used = np.full_like(self.img, False)
        clusters = collections.deque()

        for (i, j) in zip(points[0], points[1]):
            ##print(used[i,j], (i,j))
            if used[i,j]: continue
            ##print(f"\n===={i,j}====\n")
            tmp = collections.deque()
            clust = collections.deque()
            tmp.append((i, j))
            clust.append((i, j))
            used[i,j] = True
            while not len(tmp)==0:
                ##print(tmp)
                pt = tmp.pop()
                si = max(erea_start, pt[0]-size)
                ei = min(erea_end, pt[0]+size)
                sj = max(erea_start, pt[1]-size)
                ej = min(erea_end, pt[1]+size)
                # erea = self.img[si:ei+1, sj:ej+1]
                # print((i,j),erea)
                grid_i, grid_j = np.meshgrid(range(si,ei+1), range(sj,ej+1), indexing='ij')
                ##print(grid_i, grid_j)
                dis_i = (grid_i-pt[0])**2
                ##print(dis_i)
                dis_j = (grid_j-pt[1])**2
                ##print(dis_j)
                dis_filter = np.sqrt(dis_i+dis_j)<=size
                ### f = np.where(np.logical_and(self.img[si:ei+1, sj:ej+1]>=255, dis_filter))
                f = np.where(np.logical_and(self.img[si:ei+1, sj:ej+1]==0, dis_filter))
                ##print(f)

                for (ii, jj) in zip(f[0], f[1]):
                    tmp_p = (grid_i[ii,jj], grid_j[jj,jj])
                    ##print(tmp_p)
                    if used[tmp_p]: continue
                    used[tmp_p] = True
                    ##print(tmp_p,"2")
                    tmp.append(tmp_p)
                    clust.append(tmp_p)
            clusters.append(clust)

        return clusters
