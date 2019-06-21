import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Polygon, Rectangle

def main():
    sample1 = "2019-06-05_sample.map.pgm"
    img = cv2.imread(sample1, cv2.IMREAD_GRAYSCALE)
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(contours, hierarchy)
    plt.gray()
    plt.imshow(img)

    fig, ax = plt.subplots(figsize=(6, 6))
    draw_contours(ax, img, contours)
    plt.show()

def draw_contours(ax, img, contours):
    ax.imshow(img)
    ax.axis('off')
    for i, cnt in enumerate(contours):
        cnt = np.squeeze(cnt, axis=1)  # (NumPoints, 1, 2) -> (NumPoints, 2)
        # 輪郭の点同士を結ぶ線を描画する。
        ax.add_patch(Polygon(cnt, color='b', fill=None, lw=2))
        # 輪郭の点を描画する。
        ax.plot(cnt[:, 0], cnt[:, 1], 'ro', mew=0, ms=4)
        # 輪郭の番号を描画する。
        ax.text(cnt[0][0], cnt[0][1], i, color='orange', size='20')

if __name__ == "__main__":
    main()