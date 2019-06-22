import cv2
import numpy as np
import os
import sys
import queue

path = os.path.dirname(__file__)

class convex_abstraction():
    def __init__(self, mp, body_size):
        self.mp = mp
        self.cell_size = body_size
        self.half = body_size // 2
    
    def get_area(self, ij):
        return self.mp[ij[0]-self.half:ij[0]+self.half+1, ij[1]-self.half:ij[1]+self.half+1]

    def full(self, area):
        blacks = np.where(area==255) ## expect type of tuple
        focus_point = (blacks[0][0], blacks[1][0])
        

