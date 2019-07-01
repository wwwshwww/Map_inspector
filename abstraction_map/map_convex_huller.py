import cv2
import numpy as np
import os
import sys
import collections
import math
import matplotlib.pyplot as plt
from cluster import point_cluster

this_path = os.path.dirname(__file__)

def fill_convex(img, points):
    angles = np.zeros([len(points)])
    angles[0] = -999
    for i in range(1,len(angles)):
        angles[i] = get_angle(points, 0, i)
    index = np.argsort(angles)
    print(angles, index)

    hull = collections.deque()
    hull.append(index[0])
    hull.append(index[1])

    vec = lambda m, s: [points[s][0]-points[m][0], points[s][1]-points[m][1]]

    for i in range(2, len(index)):
        while True:
            tmpi = hull.pop()
            last = hull[-1]
            tcross = np.cross(vec(last,tmpi), vec(tmpi,index[i]))
            print(tmpi, index[i], tcross)
            if tcross >= 0:
                hull.append(tmpi)
                hull.append(index[i])
                break

    convex_pts = np.zeros([len(hull), 2], dtype=int)
    count = 0
    for i in hull:
        convex_pts[count] = (points[i][1], points[i][0])
        count += 1

    # newimg = cv2.polylines(img, convex_pts.reshape((1,-1,2)), True, 100)
    newimg = cv2.fillConvexPoly(img, convex_pts.reshape((1,-1,2)), 100)
    # newimg = cv2.UMat.get(newimg)
    return newimg

def get_angle(points, p1, p2): # p1, p2 : index
    dx = points[p2][0] - points[p1][0]
    dy = points[p2][1] - points[p1][1]
    return math.atan2(dy,dx)

def main():
    path = this_path + 'map_data/2019-06-05_sample2.map.pgm'
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    
    plt.gray()
    plt.imshow(img)
    plt.show()

    c = point_cluster(img)
    cb = c.get_clusters_black(size=8)
    newimg = img.copy()
    for o in cb:
        if len(o) < 2: continue
        newimg = fill_convex(newimg, list(o))

    plt.imshow(newimg)
    plt.show()
        
if __name__ == "__main__":
    main()
