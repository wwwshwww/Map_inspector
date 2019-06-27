import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

def main():
    a = np.zeros([50,50], dtype=int)
    a[5,15] = 255
    a[10,10] = 255
    a[10,20] = 255
    a[15,15] = 255
    
    points = np.where(a>=1)
    print(points)

    mpt = (points[0][0], points[1][0])
    print(mpt)

    crosses = np.zeros([len(points[0])])
    for i in range(len(crosses)):
        crosses[i] = np.cross(mpt, [points[0][i], points[1][i]])
    print(crosses)

    vec = lambda m, s: [points[0][s]-points[0][m], points[1][s]-points[1][m]]

    v1 = vec(0,1)
    v2 = vec(1,3)

    print(v1, v2, np.cross(v1,v2))
    print(v2, vec(3,2), np.cross(v2, vec(3,2)))
    print(vec(2,1), vec(1,0), np.cross(vec(2,1), vec(1,0)))
    
    show(a)

def show(img):
    plt.gray()
    plt.imshow(img)
    plt.show()

if __name__ == "__main__":
    main()