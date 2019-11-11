import numpy as np
import os
import cv2
import sys
import matplotlib.pyplot as plt

from cluster import point_cluster

this_path = os.path.dirname(__file__)
WHITE = 255

class ob_map():
    def __init__(self, map_img):
        self.map_img = map_img

    def trim(self, start: tuple, end: tuple) -> np.ndarray:
        return self.map_img[start[0]:end[0]+1, start[1]:end[1]+1]

class obstacle():
    def __init__(self, ob_id, super_map: ob_map, ob_threshold=0, points=[], is_minimapping=False):
        self.ob_id = ob_id
        self.super_map = super_map
        self.ob_threshhold = ob_threshold
        self.points = points ## have coordinates of xy
        self.child = [] ## have ob_id
        ## param
        self.have_child = False
        self.is_minimapping = is_minimapping
        if self.is_minimapping:
            self.minimap_start, self.minimap_end, self.minimap = self.minimapping()

    def minimapping(self):
        lp = np.zeros_like(self.points)
        for i, p in enumerate(self.points):
            lp[i] = [p[0], p[1]]

        max_i = np.max(lp[:,0])
        min_i = np.min(lp[:,0])
        max_j = np.max(lp[:,1])
        min_j = np.min(lp[:,1])

        pt_min = (min_i,min_j)
        pt_max = (max_i,max_j)

        return pt_min, pt_max, self.super_map.trim(pt_min, pt_max)

    def get_child(self, threshhold):
        self.have_child = True
        return get_obstacles(self.minimap, threshhold)


def get_obstacles(img, threshhold) -> list:
    pc = point_cluster(img)
    om = ob_map(img)
    clusters = pc.get_clusters_black(threshhold)
    # ob_idとかちゃんとセットしよう
    obs = [None]*len(clusters)
    for i, o in enumerate(clusters):
        obs[i] = obstacle(ob_id=i, super_map=om, ob_threshold=threshhold, points=o, is_minimapping=True)
    return obs

def main():
    path = this_path + 'map_data/2019-06-05_sample2.map.pgm'
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    print(img)
    plt.gray()
    plt.imshow(img)
    plt.show()

    obs = get_obstacles(img, 3)
    
    for o in obs:
        plt.imshow(o.minimap)
        plt.show()
    

if __name__ == "__main__":
    main()
