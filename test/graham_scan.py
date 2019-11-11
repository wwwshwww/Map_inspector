import numpy as np
import math
import collections
import cv2
import matplotlib.pyplot as plt

def main():
    a = np.zeros([50,50], dtype=int)
    a[2,2] = 255
    a[2,3] = 255
    a[1,2] = 255
    a[1,1] = 255
    a[4,35] = 255
    a[42,7] = 255
    a[42,8] = 255
    a[43,7] = 255
    a[43,8] = 255
    a[48, 40] = 255
    a[25,1] = 255
    a[22,26] = 255
    a[23,25] = 255

    points = np.where(a>=1)
    print(points)

    fp = (points[0][0], points[1][0])
    print(fp)

    angles = np.zeros_like(points[0], dtype=float)
    angles[0] = -999
    for i in range(1,len(angles)):
        angles[i] = get_angle(points, 0, i)
    index = np.argsort(angles)
    print(angles, index)

    hull = collections.deque()
    hull.append(index[0])
    hull.append(index[1])

    vec = lambda m, s: [points[0][s]-points[0][m], points[1][s]-points[1][m]]

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

    plt.gray()
    plt.imshow(a)
    plt.show()

    convex_pts = np.zeros([len(hull), 2], dtype=int)
    count = 0
    for i in hull:
        convex_pts[count] = (points[1][i], points[0][i])
        count += 1
    print(convex_pts.reshape((1,-1,2)))
    # img = cv2.polylines(a, convex_pts.reshape((1,-1,2)), True, 255)
    img = cv2.fillConvexPoly(a, convex_pts.reshape((1,-1,2)), 255)
    img = cv2.UMat.get(img)
    plt.imshow(img)
    plt.show()
    print(hull)


def get_angle(points, p1, p2): # p1, p2 : index
    dx = points[0][p2] - points[0][p1]
    dy = points[1][p2] - points[1][p1]
    return math.atan2(dy,dx)

def normalize(rad):
    ret = rad % math.pi
    if ret < 0: ret += math.pi
    return ret
    
if __name__ == "__main__":
    main()