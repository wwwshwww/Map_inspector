import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Polygon, Rectangle

def main():
    sample1 = "2019-06-05_sample.map.pgm"
    img = cv2.imread(sample1, cv2.IMREAD_GRAYSCALE)
    print(img[2000-100:2000+100, 2000-100:2000+100])
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(contours, hierarchy)
    plt.gray()
    plt.imshow(img)
    plt.show()

if __name__ == "__main__":
    main()